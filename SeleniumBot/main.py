from bookings.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.change_cur(currency="USD")
    bot.change_cur(currency="GBP")
    bot.initial_place(choose_loc="japan")
    bot.select_date(check_in="2021-10-11", check_out="2021-10-17")
    bot.select_users(4)
    bot.clk_search()
    print("exiting...")