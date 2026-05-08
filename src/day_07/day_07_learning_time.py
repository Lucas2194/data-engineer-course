day_minutes = int(input("Napisz, ile dziennię się uczysz: "))
days = int(input("Napisz ile dni masz zamiar się uczyć: "))

print(f'Masz zamiar się uczyć {day_minutes * days} minut, jest to {round((day_minutes * days)/60, 2)} godzin')