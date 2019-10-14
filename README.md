# Homobiles API 

Note: 
Every request returns an http is an int http status code, i.e. 200, 500, etc.
Every request is sent with a user_auth_token that is linked with a hardware ID (i.e. MAC addresss).

    curl https://api.homobiles.org/v1/riders \
        -u [TOKEN]: \
        -d amount=2000 \
        -d currency=usd \
        -d description="Charge for jenny.rosen@example.com" \
        -d source=tok_mastercard

### Admin API

    curl https://api.homobiles.org/v1/admin/research/:name
    curl https://api.homobiles.org/v1/admin/messages

### Rider API

Routes:

    curl https://api.homobiles.org/v1/riders/monitoring
    curl https://api.homobiles.org/v1/riders/account
    curl https://api.homobiles.org/v1/riders/rides
    curl https://api.homobiles.org/v1/riders/admin
    curl https://api.homobiles.org/v1/riders/payments

Spec. sheet:

    Page 1: ON-LOAD         GET     error               riders.monitoring.pre_flight_checks()
    Page 2:                 POST    void                riders.monitoring.indicate_allowed_location_access(bool allowed)
    Page 3:                 POST    error               riders.account.add_phone_number(int phone_number)
    Page 4:                 POST    bool                riders.account.verify_phone_number_verification_code(int verification_code)
    Page 5: ON-LOAD         GET     bool                riders.rides.check_current_location_availibility(float lat, float lng)
    Page 6: ON-LOAD         GET     []location          riders.account.get_bookmark_locations()
                            POST    location            riders.rides.search_location_query(string location_query)
                            POST    ride_request_token  riders.rides.request_ride(float start_lat, float start_lng, float end_lat, float end_lng, int time_from_now)
                            POST    void                riders.monitoring.log_user_error(error error)
    Page 7: "
    Page 8: ON-LOAD         GET     []location          riders.account.get_bookmark_locations()
                            POST    location            riders.rides.search_location_query(string location_query)
                            POST    ride_request_token  riders.rides.request_ride(float start_lat, float start_lng, float end_lat, float end_lng, int time_from_now)
                            POST    void                riders.monitoring.log_user_error(error error)
    Page 9: "
    Page 10: "
    Page 11: ON-LOAD        GET     error               riders.account.verify_account_is_rider_ready()
    Page 11a: "
    Page 11b: ON-LOAD       GET     account             riders.account.load_account()
    Page 11c: "
    Page 11d:               POST    error               riders.account.register_account_payment_method_paypal(...?)
    Page 11e:               POST    error               riders.account.register_account_payment_method_credit_card(int credit_card_number, int exp_month, int exp_year, int zip_code, int cvv)
    Page 11f:               POST    error               riders.account.register_account_payment_method_apple_pay(...?)
    Page 12:                GET     profile             riders.account.load_profile()
    Page 13:                POST    error               riders.account.save_profile(string name, string pronoun, string accomodations, string photo_filename)
    Page 14: "
    Page 15: "
    Page 16: ON-LOAD        GET     []contact           riders.account.load_trusted_contacts()
    Page 17:                POST    error               riders.account.add_trusted_contact(string contact_name, int contact_phone_number)
    Page 18:                POST    error               riders.monitoring.log_trusted_contact_message(trip_status trip_status, string contact_name, int contact_number, string text_msg, bool free_ride_sent)
    Page 19:                POST    pymt_token          riders.payments.initialize_one_time_donation(int donation_amount, bool round_up)
    Page 20: "
    Page 21:                POST    error               riders.payments.confirm_one_time_donation_paypal(pymt_token payment_token)
    Page 22:                POST    error               riders.account.register_account_payment_method_credit_card(int credit_card_number, int exp_month, int exp_year, int zip_code, int cvv)
    Page 23:                POST    error               riders.payments.confirm_one_time_donation_credit_card(pymt_token payment_token)
    Page 24:                POST    document            riders.account.request_tax_deductable_reciept(string email_address)
    Page 25: ON-LOAD        GET     page                riders.admin.load_about_us_page()
    Page 26: ON-LOAD        GET     page                riders.admin.load_help_menu()
    Page 27: ON-LOAD        GET     page                riders.admin.load_report_a_ride_form()
                            POST    error               riders.admin.report_a_ride(string message)
    Page 28: "
    Page 29: ON-LOAD        GET     page                riders.admin.load_report_a_lost_item_form()
                            POST    error               riders.admin.report_a_lost_item(string message)
    Page 30: "
    Page 31:                GET     page                riders.admin.load_how_payment_works_page()
    Page 32:                GET     page                riders.admin.load_how_do_free_rides_work_page()
    Page 33:                GET     page                riders.admin.load_saftey_page()
    Page 34:                GET     page                riders.admin.load_policies_page()
    Page 35:                GET     page                riders.admin.load_legal_page()
    Page 36:                GET     []ride              riders.account.load_past_rides(int limit, int offset)
    Page 37: "
    Page 38:                POST    error               riders.payments.add_a_driver_tip(ride ride, int tip_amount)
    Page 39: "
    Page 40: "
    Page 41: ON-LOAD        GET     []ride              riders.account.load_past_rides(int limit, int offset)
    Page 42: ON-LOAD        GET     settings            riders.account.load_settings()
    Page 43: NA
    Page 44: NA
    Page 45: NA
    Page 46:                POST    error               riders.account.update_email_address(string email_address)
    Page 47:                POST    error               riders.account.add_accessibility_requirements(int accessibility_requirment_key)
                            POST    error               riders.account.remove_accessibility_requirements(int accessibility_requirment_key)
    Page 48:                POST    error               riders.account.update_phone_number(int phone_number)
                            POST    bool                riders.account.verify_phone_number_verification_code(int verification_code)
    Page 49:                POST    void                riders.monitoring.log_location_permission_change(bool on)
    Page 50:                POST    void                riders.monitoring.log_contacts_permission_change(bool on)
    Page 51:                POST    error               riders.account.log_out()
    Page 52:                POST    error               riders.account.unregister()
    Page 53:                POST    void                riders.monitoring.log_notifications_permission_change(bool on)
    Page 54: ON-LOAD        GET     ride_estimate       riders.rides.load_ride_request_estimate(ride_request_token ride_request_token)
    Page 55: NONE
    Page 56: NONE
    Page 57: NONE
    Page 58:                POST    error               riders.rides.confirm_ride_requet(ride_request_token ride_request_token)
    Page 59: ON-LOAD        GET     live_ride           riders.rides.load_live_ride(ride_request_token ride_request_token)
    Page 59: ON-LONG-POLE   GET     live_ride           riders.rides.load_live_ride(ride_request_token ride_request_token)
    Page 61:                POST    error               riders.rides.post_live_ride_pickup_note(string pickup_note)
                            POST    error               riders.rides.cancel_ride(ride_request_token ride_request_token)
                            POST    location            riders.rides.search_location_query(string location_query)
                            POST    error               riders.rides.edit_ride_destination(ride_request_token ride_request_token, float lat, float lng)
    Page 62: NONE
    Page 63: ON-LONG-POLE   GET     live_ride           riders.rides.load_live_ride(ride_request_token ride_request_token)
                            POST    error               riders.rides.share_trip_status(ride_request_token ride_request_token, float lat, float lng)
                            POST    void                riders.monitor.log_share_trip_status(ride_request_token ride_request_token, float lat, float lng)
    Page 64:                POST    void                riders.monitor.log_911_assistance_opened(ride_request_token ride_request_token, float lat, float lng) 
                            POST    void                riders.monitor.log_911_assistance_called(ride_request_token ride_request_token, float lat, float lng)
    Page 65: ON-LONG-POLE   GET     live_ride           riders.rides.share_trip_status(ride_request_token ride_request_token, float lat, float lng)
    Page 66:                POST    error               riders.rides.rate_ride(ride_request_token ride_request_token, ride_rating ride_rating)
                            POST    error               riders.payments.leave_driver_tip(ride_request_token ride_request_token, int tip_amount)
    Page 67:                POST    error               riders.rides.post_ride_feedback(ride_request_token ride_request_token, string ride_feedback)
    Page 67A:               POST    error               riders.rides.post_last_ride_message_to_driver(ride_request_token ride_request_token, string ride_feedback)

All methods:
    
    GET     riders.monitoring.pre_flight_checks()
    POST    riders.monitoring.indicate_allowed_location_access(bool allowed)
    POST    riders.account.add_phone_number(int phone_number)
    POST    riders.account.verify_phone_number_verification_code(int verification_code)
    GET     riders.rides.check_current_location_availibility(float lat, float lng)
    GET     riders.account.get_bookmark_locations()
    POST    riders.rides.search_location_query(string location_query)
    POST    riders.rides.request_ride(float start_lat, float start_lng, float end_lat, float end_lng, int time_from_now)
    POST    riders.monitoring.log_user_error(error error)
    GET     riders.account.verify_account_is_rider_ready()
    GET     riders.account.load_account()
    POST    riders.account.register_account_payment_method_paypal(...?)
    POST    riders.account.register_account_payment_method_credit_card(int credit_card_number, int exp_month, int exp_year, int zip_code, int cvv)
    POST    riders.account.register_account_payment_method_apple_pay(...?)
    GET     riders.account.load_profile()
    POST    riders.account.save_profile(string name, string pronoun, string accomodations, string photo_filename)
    GET     riders.account.load_trusted_contacts()
    POST    riders.account.add_trusted_contact(string contact_name, int contact_phone_number)
    POST    riders.monitoring.log_trusted_contact_message(trip_status trip_status, string contact_name, int contact_number, string text_msg, bool free_ride_sent)
    POST    riders.payments.initialize_one_time_donation(int donation_amount, bool round_up)
    POST    riders.payments.confirm_one_time_donation_paypal(pymt_token payment_token)
    POST    riders.payments.confirm_one_time_donation_credit_card(pymt_token payment_token)
    POST    riders.account.request_tax_deductable_reciept(string email_address)
    GET     riders.admin.load_about_us_page()
    GET     riders.admin.load_help_menu()
    GET     riders.admin.load_report_a_ride_form()
    POST    riders.admin.report_a_ride(string message)
    GET     riders.admin.load_report_a_lost_item_form()
    POST    riders.admin.report_a_lost_item(string message)
    GET     riders.admin.load_how_payment_works_page()
    GET     riders.admin.load_how_do_free_rides_work_page()
    GET     riders.admin.load_saftey_page()
    GET     riders.admin.load_policies_page()
    GET     riders.admin.load_legal_page()
    GET     riders.account.load_past_rides(int limit, int offset)
    POST    riders.payments.add_a_driver_tip(ride ride, int top_amount)
    GET     riders.account.load_settings()
    POST    riders.account.update_email_address(string email_address)
    POST    riders.account.add_accessibility_requirements(int accessibility_requirment_key)
    POST    riders.account.remove_accessibility_requirements(int accessibility_requirment_key)
    POST    riders.account.update_phone_number(int phone_number)
    POST    riders.monitoring.log_location_permission_change(bool on)
    POST    riders.monitoring.log_contacts_permission_change(bool on)
    POST    riders.account.log_out()
    POST    riders.account.unregister()
    POST    riders.monitoring.log_notifications_permission_change(bool on)
    GET     riders.rides.load_ride_request_estimate(ride_request_token ride_request_token)
    POST    riders.rides.confirm_ride_requet(ride_request_token ride_request_token)
    GET     riders.rides.load_live_ride(ride_request_token ride_request_token)
    POST    riders.rides.post_live_ride_pickup_note(string pickup_note)
    POST    riders.rides.cancel_ride(ride_request_token ride_request_token)
    POST    riders.rides.edit_ride_destination(ride_request_token ride_request_token, float lat, float lng)
    POST    riders.rides.share_trip_status(ride_request_token ride_request_token, float lat, float lng)
    POST    riders.monitor.log_share_trip_status(ride_request_token ride_request_token, float lat, float lng)
    POST    riders.monitor.log_911_assistance_opened(ride_request_token ride_request_token, float lat, float lng) 
    POST    riders.monitor.log_911_assistance_called(ride_request_token ride_request_token, float lat, float lng)
    POST    riders.rides.rate_ride(ride_request_token ride_request_token, ride_rating ride_rating)
    POST    riders.payments.leave_driver_tip(ride_request_token ride_request_token, int tip_amount)
    POST    riders.rides.post_ride_feedback(ride_request_token ride_request_token, string ride_feedback)
    POST    riders.rides.post_last_ride_message_to_driver(ride_request_token ride_request_token, string ride_feedback)

### Driver API

Routes:
    
    curl https://api.homobiles.org/v1/drivers/account
    curl https://api.homobiles.org/v1/drivers/monitoring
    curl https://api.homobiles.org/v1/drivers/status
    curl https://api.homobiles.org/v1/drivers/rides

Spec. sheet:


    Page A1: ON-LOAD        GET     error               drivers.monitoring.pre_flight_checks()
    Page A2:                POST    void                drivers.monitoring.indicate_allowed_location_access(bool allowed)
    Page A3:                POST    error               drivers.account.add_phone_number(int phone_number)
    Page A4:                POST    bool                drivers.account.verify_phone_number_verification_code(int verification_code)
    Page A5: ON-LOAD        GET     error               drivers.account.verify_account_is_driver_ready()
    Page A6: ON-LOAD        GET     account             drivers.account.load_account()
    Page A7:                POST    account             drivers.account.update_account(string name,
                                                                                    string pronouns,
                                                                                    string vehicle_make_and_model,
                                                                                    string vehicle_color,
                                                                                    int    vehicle_year,
                                                                                    string vehicle_licence_plate,
                                                                                    string smartphone_type,
                                                                                    string smartphone_carrier,
                                                                                    string profile_photo_filename,
                                                                                    string vehicle_photo_filename,
                                                                                    bool   have_insurance,
                                                                                    bool   concent_drugtest_background,
                                                                                    string fact1,
                                                                                    string fact2,
                                                                                    string fact3)

    Page 1: ON-LOAD         POST    error               drivers.monitoring.pre_flight_checks()
            ON-LOAD         GET     driver_status       drivers.status.load_status()
                            POST    error               drivers.status.go_online()
    Page 2: ON-LONG-POLE    GET     driver_status       drivers.status.load_status()
                            POST    driver_status       drivers.status.go_offline()
    Page 3: ON-LONG-POLE    GET     driver_status       drivers.status.load_status()
                            POST    rides               drivers.rides.accept_ride_request(ride_request_token ride_request_token)
    Page 4: ON-LONG-POLE    GET     driver_status       drivers.status.load_status()
    Page 5:                 POST    rides               drivers.rides.display_ride_color_number_card(ride_request_token ride_request_token)
    Page 6:                 POST    rides               drivers.rides.start_ride(ride_request_token ride_request_token)
    Page 7:                 POST    rides               drivers.rides.end_ride(ride_request_token ride_request_token)

All methods:
    
    POST    drivers.monitoring.pre_flight_checks()
    GET     drivers.status.load_status()
    POST    drivers.status.go_online()
    POST    drivers.status.go_offline()
    POST    drivers.rides.accept_ride_request(ride_request_token ride_request_token)
    POST    drivers.rides.display_ride_color_number_card(ride_request_token ride_request_token)
    POST    drivers.rides.start_ride(ride_request_token ride_request_token)
    POST    drivers.rides.end_ride(ride_request_token ride_request_token)
