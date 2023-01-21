/**
 * @file Complementar script for products admin page.
 *
 */
/* global Cropper, Mustache */
(function (root, factory) {
    if (typeof define === 'function' && define.amd) {
        // AMD. Register as an anonymous module.
        define(['jquery'], factory);
    } else if (root.mainApp.controller) {
        // Set as a module for the controller
        root.mainApp.controller.module = factory(mainApp.controller, window.jQuery || window.$);
    } else if (root.mainApp) {
        // Set as a controller for main application
        root.mainApp.controller = factory(mainApp, window.jQuery || window.$);
    } else {
        // Browser globals
        console.error('Main application was not loaded'); // eslint-disable-line
    }
}(typeof self !== 'undefined' ? self : this, function (parent, $) {
    'use strict';

    $('#refresh').on('click', (evt) => {
        evt.preventDefault();

        mainApp.ajax({
            url: `delivery`,
            method: 'PUT',
            data: {
                'delivery_tax': $('#edit-delivery').val()
            },
            dataType: 'json',
            success: () => {

            },
            error: () => {
            }
        });

        let url = 'http://127.0.0.1:5000/delivery_fee/';
        let xhr = new XMLHttpRequest();
        xhr.open('PUT', url, true);
        xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhr.send(JSON.stringify({ "value": $('#edit-delivery').val()}));

    });

    /**
     * Creates the module.
     * @class
     */
    return {
        /**
         * Initiates the module.
         */
        init: () => {
        },
    };
}));