def boarding_passengers(capacity, *passenger_groups):
    boarded_passengers = {}
    total_boarded = 0

    sorted_passenger_groups = sorted(passenger_groups, key=lambda x: (-x[0], x[1]))

    for passengers, benefit_program in sorted_passenger_groups:
        if capacity == 0:
            break

        if passengers <= capacity:
            if benefit_program in boarded_passengers:
                boarded_passengers[benefit_program] += passengers
            else:
                boarded_passengers[benefit_program] = passengers

            total_boarded += passengers
            capacity -= passengers

    output = []
    for benefit_program, count in sorted(boarded_passengers.items(), key=lambda x: (-x[1], x[0])):
        output.append(f"## {benefit_program}: {count} guests")

    if total_boarded == sum(group[0] for group in passenger_groups):
        output.append("All passengers are successfully boarded!")
    elif capacity == 0:
        output.append("Boarding unsuccessful. Cruise ship at full capacity.")
    else:
        output.append(f"Partial boarding completed. Available capacity: {capacity}.")

    return "\n".join(output)


print("Boarding details by benefit plan:")

# Practice 1 Test case where all passengers can be boarded
from unittest import TestCase, main


class TestBoardingPassengers(TestCase):
    def test_boarding_passengers(self):
        result = boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser'))
        expected = """Boarding details by benefit plan:
## Platinum: 55 guests
## Diamond: 35 guests
## Gold: 35 guests
## First Cruiser: 25 guests
All passengers are successfully boarded!"""
        self.assertEqual(result.strip(), expected)