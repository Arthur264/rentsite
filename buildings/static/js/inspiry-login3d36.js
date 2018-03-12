(function($) {

    "use strict";

    $(document).ready(function() {

        var progress_bar = new ProgressBar.Line('#rh_progress', {
            easing: 'easeInOut',
            color: '#1ea69a',
            strokeWidth: 0.3,
        });

        var modal_switch = $('div.switch');
        var modal_switch_link = modal_switch.find('a');

        modal_switch_link.click(function(e) {

            e.preventDefault(); // Prevent default.

            var switch_to = $(this).attr('data-switch'); // Switch to modal.
            var target = '';

            if ('forgot' === switch_to) {

                var switch_parent = $(this).parents('div.modal');
                target = $('div.rh_modal__forgot_wrap');
                switch_parent.slideToggle('slow');
                target.slideToggle('slow');

            } else if ('register' === switch_to) {

                var switch_parent = $(this).parents('div.modal');

                target = $('div.rh_modal__register_wrap');
                switch_parent.slideToggle('slow');
                target.slideToggle('slow');

            } else if ('login' === switch_to) {

                var switch_parent = $(this).parents('div.modal');

                target = $('div.rh_modal__login_wrap');
                switch_parent.slideToggle('slow');
                target.slideToggle('slow');

            }
        });

        if (jQuery().validate && jQuery().ajaxSubmit) {

            /**
             * AJAX Login Form
             */
            var loginButton = $('#login-button'),
                // loginAjaxLoader = $('#login-loader'),
                loginError = $("#login-error"),
                loginMessage = $('#login-message');

            var loginOptions = {
                beforeSubmit: function() {
                    progress_bar.set(0);
                    progress_bar.animate(1);
                    loginMessage.fadeOut(50);
                    loginError.fadeOut(50);
//                    loginButton.attr('disabled', 'disabled');
                    // loginAjaxLoader.fadeIn( 200 );
                },
                success: function(ajax_response, statusText, xhr, $form) {
                    var response = ajax_response;
                    // loginAjaxLoader.fadeOut( 100 );
                    loginButton.removeAttr('disabled');
                    if (response.success) {
                     var list = document.createElement("ul");
                        for (var prop in response.message) {
                            for (var i = 0; i < response.message[prop].length; i++) {
                                var li = document.createElement("li");
                                li.innerHTML = response.message[prop][i];
                                list.appendChild(li)
                            }
                        }
                        loginMessage.html(list).fadeIn(200);
                        location.reload();
                    } else {
                        loginError.html(response.message).fadeIn(200);

                        // call reset function if it exists
                        if (typeof inspiryResetReCAPTCHA == 'function') {
                            inspiryResetReCAPTCHA();
                        }
                    }
                }
            };

            $('#rh_modal__login_form').validate({
                submitHandler: function(form) {
                    $(form).ajaxSubmit(loginOptions);
                }
            });

            /**
             * AJAX Register Form
             */
            var registerButton = $('#register-button'),
                // registerAjaxLoader = $('#register-loader'),
                registerError = $("#register-error"),
                registerMessage = $('#register-message');

            var registerOptions = {
                beforeSubmit: function() {
                    progress_bar.set(0);
                    progress_bar.animate(1);
                    //                    registerButton.attr('disabled', 'disabled');
                    // registerAjaxLoader.fadeIn('fast');
                    registerMessage.fadeOut('fast');
                    registerError.fadeOut('fast');
                },
                success: function(ajax_response, statusText, xhr, $form) {
                    var response = $.parseJSON(ajax_response);
                    // registerAjaxLoader.fadeOut('fast');
                    registerButton.removeAttr('disabled');
                    if (response.success) {
                        registerMessage.html(response.message).fadeIn('fast');
                        $form.resetForm();
                        location.reload();
                    } else {
                        var list = document.createElement("ul");
                        for (var prop in response.message) {
                            for (var i = 0; i < response.message[prop].length; i++) {
                                var li = document.createElement("li");
                                li.innerHTML = response.message[prop][i];
                                list.appendChild(li)
                            }
                        }
                        registerError.html(list).fadeIn('fast');
                        // call reset function if it exists
                        if (typeof inspiryResetReCAPTCHA == 'function') {
                            inspiryResetReCAPTCHA();
                        }
                    }
                }
            };

            $('#rh_modal__register_form').validate({
                rules: {
                    username: {
                        required: true
                    },
                    email: {
                        required: true,
                        email: true
                    },
                    password1: {
                        required: true,
                        minlength: 8
                    },
                    password2: {
                        required: true,
                        equalTo: "#password1"
                    }
                },
                submitHandler: function(form) {
                    $(form).ajaxSubmit(registerOptions);
                }
            });


            /**
             * Forgot Password Form
             */
            var forgotButton = $('#forgot-button'),
                // forgotAjaxLoader = $('#forgot-loader'),
                forgotError = $("#forgot-error"),
                forgotMessage = $('#forgot-message');

            var forgotOptions = {
                beforeSubmit: function() {
                    progress_bar.set(0);
                    progress_bar.animate(1);
                    forgotButton.attr('disabled', 'disabled');
                    // forgotAjaxLoader.fadeIn('fast');
                    forgotMessage.fadeOut('fast');
                    forgotError.fadeOut('fast');
                },
                success: function(ajax_response, statusText, xhr, $form) {
                    var response = $.parseJSON(ajax_response);
                    // forgotAjaxLoader.fadeOut('fast');
                    forgotButton.removeAttr('disabled');
                    if (response.success) {
                        forgotMessage.html(response.message).fadeIn('fast');
                        $form.resetForm();
                    } else {
                        forgotError.html(response.message).fadeIn('fast');

                        // call reset function if it exists
                        if (typeof inspiryResetReCAPTCHA == 'function') {
                            inspiryResetReCAPTCHA();
                        }
                    }
                }
            };

            $('#rh_modal__forgot_form').validate({
                submitHandler: function(form) {
                    $(form).ajaxSubmit(forgotOptions);
                }
            });

        }

        /**
         * Forgot Form
         */
        $('.rh_form #rh_modal__forgot_form').slideUp('fast');
        $('.rh_form .toggle-forgot-form').click(function(event) {
            event.preventDefault();
            $('.rh_form #rh_modal__forgot_form').slideToggle('fast');
        });

    });

})(jQuery);