### Need to do some bringing in of packages, loading libraries etc here
### Also some blurb about what it is we are doing

# Set up global class (numbers just placeholders for now)
class g:
    time_units_between_customer_arrivals = 5
    mean_diagnostic_test_time = 6
    number_of_receptionists
    number_of_clinicians = 1
    sim_duration = 1440
    number_of_runs = 10

# Create 'patient' class
class Patient:
    def __init__(self, p_id):
        self.id = p_id
        self.queue_time_clinician = 0

# Create 'receptionist' class
class Receptionist:
    def __init__(self, p_id):
        self.id = p_id
        # self.queue_time_customer_support_agent = 0 <- fix this

# Create 'clinician' class
class Clinician:
    def __init__(self, p_id):
        self.id = p_id
        # self.queue_time_customer_support_agent = 0 <- fix this