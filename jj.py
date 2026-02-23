from baladia.main_printer import print_full_bundle

personelinfo = {
    "ccp": "444444",
    "cle": "69",
    "first_name": "تالاتلات",
    "last_name": "تالاتلات",
    "birth_date": "25-20-3838",
    "birth_place": "تالاتلات",
    "address": "تالاتلات",
    "national_id": "34567890567890-",
    "id_issue_date": "888888-880-888",
    "phone": "23456789989",
}

monthlypay = {
    "amount_1": "2777",
    "rate_1": "2222",
    "amount_2": "222",
    "rate_2": "222",
    "months": "27",
    "discount": "222",
    "total_raw": "222",
    "final_total": "222",
    "monthly_cut": "222",
    "datecute": "",
}
print_full_bundle(personelinfo, monthlypay)
