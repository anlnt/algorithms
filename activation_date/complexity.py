import collections

Record = collections.namedtuple('Record', 'phone_number activation_date deactivation_date')
dataset = [
  Record(phone_number="0987000001",activation_date="2016-03-01",deactivation_date="2016-05-01"),
  Record(phone_number="0987000002",activation_date="2016-02-01",deactivation_date="2016-03-01"),
  Record(phone_number="0987000001",activation_date="2016-01-01",deactivation_date="2016-03-01"),
  Record(phone_number="0987000001",activation_date="2016-12-01",deactivation_date=""),
  Record(phone_number="0987000002",activation_date="2016-03-01",deactivation_date="2016-05-01"),
  Record(phone_number="0987000003",activation_date="2016-01-01",deactivation_date="2016-01-10"),
  Record(phone_number="0987000001",activation_date="2016-09-01",deactivation_date="2016-12-01"),
  Record(phone_number="0987000002",activation_date="2016-05-01",deactivation_date=""),
  Record(phone_number="0987000001",activation_date="2016-06-01",deactivation_date="2016-09-01")
]
# ------------------
# Mem1: N for dataset
# ------------------

phone_and_deactivation_date_set = {}
# Time: N for looping through dataset
for record in dataset:
  # Time: 1 for adding an item to hash table
  phone_and_deactivation_date_set[record.phone_number + "-" + record.deactivation_date] = "" # value can be anything
# ----------------------
# Mem2: N for hash table
# Time1: N*1 = N
# ----------------------

owner_activation_dates_of_phone_map = {}
# Time: N for looping through dataset
for record in dataset:
  # Time: 1 for looking up an item in hash table
  if not phone_and_deactivation_date_set.has_key(record.phone_number + "-" + record.activation_date):
    # Time: 1 for looking up an item in hash table
    if not owner_activation_dates_of_phone_map.has_key(record.phone_number):
      # Time: 1 for adding an item to hash table
      owner_activation_dates_of_phone_map[record.phone_number] = []
    #  Time: 1 for appending an item to a list
    owner_activation_dates_of_phone_map[record.phone_number].append(record.activation_date)
# --------------------------------------------------
# Mem3: Maximum 2*N(N keys, N values) for hash table
# Time2: N*1*(1*1 + 1) => 2*N
# --------------------------------------------------

# Time: 1 for getting all keys in the table
unique_phone_numbers = owner_activation_dates_of_phone_map.keys()
# Time: N*logN for sorting all items
for phone_number in unique_phone_numbers:
  activation_dates = sorted(owner_activation_dates_of_phone_map[phone_number])
  print(phone_number, activation_dates[-1])
# ------------------------------------------------------------
# Mem4: N for merge sort and N for unique_phone_numbers => 2*N
# Time3: 1 + N*logN
# ------------------------------------------------------------

# Total
# Time = Time1 + Time2 + Time3 = N + 2*N + 1 + N*logN = N*logN
# Mem = Mem1 + Mem2 + Mem3 + Mem4 = N + N + 2N + N + N = N
