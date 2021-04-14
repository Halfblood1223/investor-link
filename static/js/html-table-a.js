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

            var datatable = $('#kt_datatable_a').KTDatatable({
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
                        field: 'Score',
                        title: 'Score',
                        autoHide: false,
                        // callback function support for column rendering
                        template: function(row) {
                            var status = {
                                1: {
                                    'title': '70%',
                                    'class': ' label-light-warning'
                                },
                                2: {
                                    'title': '75%',
                                    'class': ' label-light-danger'
                                },
                                3: {
                                    'title': '80%',
                                    'class': ' label-light-primary'
                                },
                                4: {
                                    'title': '85%',
                                    'class': ' label-light-success'
                                },
                                5: {
                                    'title': '90%',
                                    'class': ' label-light-info'
                                }
                            };
                            return '<span class="label font-weight-bold label-lg' + status[row.Score].class + ' label-inline">' + status[row.Score].title + '</span>';
                        },
                    }, {
                        field: 'Ratio',
                        title: 'Ratio',
                        autoHide: false,
                        // callback function support for column rendering
                        template: function(row) {
                            var status = {
                                1: {
                                    'title': '0.5x',
                                    'class': ' label-light-danger'
                                },
                                2: {
                                    'title': '1.0x',
                                    'class': ' label-light-primary'
                                },
                                3: {
                                    'title': '1.5x',
                                    'class': ' label-light-success'
                                },
                                4: {
                                    'title': '2.0x',
                                    'class': ' label-light-warning'
                                },
                                5: {
                                    'title': '2.5x',
                                    'class': ' label-light-info'
                                }
                            };
                            return '<span class="label font-weight-bold label-lg' + status[row.Ratio].class + ' label-inline">' + status[row.Ratio].title + '</span>';
                        },
                    },
                ],
            });



            $('#kt_datatable_search_status_a').on('change', function() {
                datatable.search($(this).val().toLowerCase(), 'Score');
            });

            $('#kt_datatable_search_type_a').on('change', function() {
                datatable.search($(this).val().toLowerCase(), 'Ratio');
            });

            $('#kt_datatable_search_status_a, #kt_datatable_search_type_a').selectpicker();

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