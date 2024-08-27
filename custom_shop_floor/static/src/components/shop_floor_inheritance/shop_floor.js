/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { MrpDisplayAction } from "@mrp_workorder/mrp_display/mrp_display_action";

patch(MrpDisplayAction.prototype, {
    get fieldsStructure() {
        const originalStructure = super.fieldsStructure;
        const modifiedStructure = { ...originalStructure };

        if (modifiedStructure["mrp.workorder"]) {
            modifiedStructure["mrp.workorder"] = [
                ...modifiedStructure["mrp.workorder"],
                "x_studio_linked_sales"
            ];
        }
        return modifiedStructure;
    },
});
