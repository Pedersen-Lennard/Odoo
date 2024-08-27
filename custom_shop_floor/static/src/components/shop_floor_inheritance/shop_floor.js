/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { MrpDisplayAction } from "@mrp_workorder/mrp_display/mrp_display_action";

patch(MrpDisplayAction.prototype, {
    get fieldsStructure() {

        const originalStructure = super.fieldsStructure;
        console.log("Original fieldsStructure:", originalStructure);

        const modifiedStructure = { ...originalStructure };

        if (modifiedStructure["mrp.production"]) {
            modifiedStructure["mrp.production"] = [
                ...modifiedStructure["mrp.production"],
                "x_record_production"
            ];
        }

        if (modifiedStructure["mrp.workorder"]) {
            modifiedStructure["mrp.workorder"] = [
                ...modifiedStructure["mrp.workorder"],
                "x_studio_linked_sales"
            ];
        }
        return modifiedStructure;
    },
});
