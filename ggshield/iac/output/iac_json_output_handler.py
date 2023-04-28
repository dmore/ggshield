from typing import Any, Dict, cast

from pygitguardian.iac_models import IaCScanResultSchema

from ggshield.iac.output.iac_output_handler import IaCOutputHandler
from ggshield.iac.output.schemas import IaCJSONScanResultSchema
from ggshield.scan import ScanCollection


class IaCJSONOutputHandler(IaCOutputHandler):
    def _process_scan_impl(self, scan: ScanCollection) -> str:
        scan_dict = IaCJSONOutputHandler.create_scan_dict(scan)
        text = IaCJSONScanResultSchema().dumps(scan_dict)
        return cast(str, text)

    @staticmethod
    def create_scan_dict(scan: ScanCollection) -> Dict[str, Any]:
        if scan.iac_result is None:
            return {
                "id": scan.id,
                "type": scan.type,
                "total_incidents": 0,
                "entities_with_incidents": [],
            }
        scan_dict: Dict[str, Any] = IaCScanResultSchema().dump(scan.iac_result)
        scan_dict["total_incidents"] = 0

        for entity in scan_dict["entities_with_incidents"]:
            total_incidents = len(entity["incidents"])
            entity["total_incidents"] = total_incidents
            scan_dict["total_incidents"] += total_incidents

        return scan_dict