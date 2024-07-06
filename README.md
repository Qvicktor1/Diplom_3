## Диплом Задание 3

Тесты UI сервиса StellarBurger

### Описание проверок:

#### 1. test_password_recovery.py 
Проверяет функциональность восстановления пароля.

Содержит тесты:
- test_click_on_pass_recovery_button_opens_pass_recovery_page
- test_input_email_and_click_on_pass_recovery_button_opens_reset_pass_page
- test_highlight_pass_entry_field


#### 2. test_account.py
Проверяет функциональность личного кабинета

Содержит тесты:
- test_click_on_account_button_opens_profile_page
- test_click_on_order_history_url_opens_orders_history_page
- test_click_on_exit_url_logs_out_from_account


#### 3. test_main.py
Проверяет основной функционал.

Содержит тесты:
- test_transition_to_constructor_and_feed_pages
- test_click_on_ingredient_opens_popup_window
- test_click_on_ingredient_details_window_close_button_closes_window
- test_increase_of_ingredient_counter
- test_authorised_user_place_order


#### 4. test_feed.py
Проверяет раздел "Лента заказов".

Содержит тесты:
- test_click_on_order_opens_details_popup_window
- test_user_order_displayed_on_feed_page
- test_increase_completed_counters
- test_order_number_displayed_in_progress_section




