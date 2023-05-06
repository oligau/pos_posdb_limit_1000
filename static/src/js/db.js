odoo.define('pos_posdb_limit_1000.pos_posdb_limit_1000', function (require) {
"use strict";
    
var { PosGlobalState } = require('point_of_sale.models');
const Registries = require('point_of_sale.Registries');


const PosDBLimit1000PosGlobalState = (PosGlobalState) => class PosDBLimit1000PosGlobalState extends PosGlobalState {
    constructor(obj) {
        super(obj);
        this.db.limit = 1000;
    }
}

Registries.Model.extend(PosGlobalState, PosDBLimit1000PosGlobalState);

});