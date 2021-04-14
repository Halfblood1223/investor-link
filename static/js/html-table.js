/******/
(() => { // webpackBootstrap
    /******/
    "use strict";
    var __webpack_exports__ = {};
    /*!*********************************************************************!*\
      !*** ../demo3/src/js/pages/features/ktdatatable/base/html-table.js ***!
      \*********************************************************************/

    // Class definition

    var KTDatatableHtmlTableDemo = function() {
        // Private functions

        // demo initializer
        var demo = function() {

            var datatable = $('#kt_datatable').KTDatatable({
                data: {
                    saveState: { cookie: false },
                },
                search: {
                    input: $('#kt_datatable_search_query'),
                    key: 'generalSearch'
                },
                columns: [{
                        field: 'DepositPaid',
                        type: 'number',
                    },
                    {
                        field: 'OrderDate',
                        type: 'date',
                        format: 'DD-MM-YYYY',
                    }, {
                        field: 'Value',
                        title: 'Value',
                        autoHide: false,
                        // callback function support for column rendering
                        template: function(row) {
                            var status = {
                                1: {
                                    'title': 'Cheaper & Easier',
                                    'class': 'label-light-primary'
                                },
                                2: {
                                    'title': 'Cheaper & Faster',
                                    'class': ' label-light-success'
                                },
                                3: {
                                    'title': 'Cheaper & Safer',
                                    'class': ' label-light-danger'
                                },
                                4: {
                                    'title': 'Easier & Faster',
                                    'class': ' label-light-info'
                                },
                                5: {
                                    'title': 'Easier & Safer',
                                    'class': ' label-light-warning'
                                },
                                6: {
                                    'title': 'Safer & Faster',
                                    'class': ' label-light-danger'
                                },
                            };
                            return '<span class="label font-weight-bold label-lg' + status[row.Value].class + ' label-inline">' + status[row.Value].title + '</span>';
                        },
                    }, {
                        field: 'Availability',
                        title: 'Availability',
                        autoHide: false,
                        // callback function support for column rendering
                        template: function(row) {
                            var status = {
                                1: {
                                    'title': 'Countywide',
                                    'class': ' label-light-danger'
                                },
                                2: {
                                    'title': 'Citywide',
                                    'class': ' label-light-primary'
                                },
                                3: {
                                    'title': 'Statewide',
                                    'class': ' label-light-success'
                                },
                                4: {
                                    'title': 'Nationwide',
                                    'class': ' label-light-warning'
                                },
                                5: {
                                    'title': 'Worldwide',
                                    'class': ' label-light-info'
                                },
                            };
                            return '<span class="label font-weight-bold label-lg' + status[row.Availability].class + ' label-inline">' + status[row.Availability].title + '</span>';
                        },
                    },
                ],
            });



            $('#kt_datatable_search_status').on('change', function() {
                datatable.search($(this).val().toLowerCase(), 'Value');
            });

            $('#kt_datatable_search_type').on('change', function() {
                datatable.search($(this).val().toLowerCase(), 'Availability');
            });

            $('#kt_datatable_search_status, #kt_datatable_search_type').selectpicker();

        };

        return {
            // Public functions
            init: function() {
                // init dmeo
                demo();
            },
        };
    }();

    jQuery(document).ready(function() {
        KTDatatableHtmlTableDemo.init();
    });

    /******/
})();
//# sourceMappingURL=html-table.js.map