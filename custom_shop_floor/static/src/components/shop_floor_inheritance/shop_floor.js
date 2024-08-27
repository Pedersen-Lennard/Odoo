/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { MrpDisplayAction } from "@mrp_workorder/mrp_display/mrp_display_action";

patch(MrpDisplayAction.prototype, {
    get fieldsStructure() {
        let res = super.fieldsStructure;
        res['mrp.production'].push('x_studio_linked_sales');
        console.log("test", res)
        return res;
    }
})