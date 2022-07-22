# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
updated_damages = []
def convert(damages):
  for i in range(len(damages)):
    scale = damages[i][-1]
    if scale == "M" or scale == "B":
      num = damages[i][:-1]
      update = str(float(num)*(conversion[scale]))
    else:
      update = damages[i]
    updated_damages.append(update)
  return updated_damages
updated_damages = convert(damages)
#print(damages)
#print(updated_damages)  

# 2 
# Create a Table

# Create and view the hurricanes dictionary
def hurr_dict(key):
  table = {}
  info = {}
  for i in range(len(names)):
    info["Name"] = names[i]
    info["Month"] = months[i]
    info["Year"] = years[i]
    info["Max Sustained Wind"] = max_sustained_winds[i]
    info["Areas Affected"] = areas_affected[i]
    info["Damage"] = damages[i]
    info["Deaths"] = deaths[i]

    table[key[i]] = info
    info = {}
  return table

name_dict = hurr_dict(names)
#print(name_dict)
#print(" ")

# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key
year_dict = hurr_dict(years)
#print(year_dict)

# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in
def area_freq(ls):
  freq = {}
  for i in ls:
    for j in i:
      if j in freq:
        freq[j] += 1
      else:
        freq[j] = 1
  return freq
affected_areas_freq = area_freq(areas_affected)
#print(affected_areas_freq)

# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def most_hit(freq):
  area = ""
  count = 0
  for k, v in freq.items():
    if v > count:
      count = v
      area = k
  return area, count
max_area, max_area_count = most_hit(affected_areas_freq)
#print(f"{max_area} was affected {max_area_count} times")

# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths
def deadliest(ls):
  name = ""
  count = 0
  for i in range(len(ls)):
    if ls[i] > count:
      count = ls[i]
      name = names[i]
  return name, count
max_mortality_cane, max_mortality = deadliest(deaths)
#print(f"{max_mortality_cane} caused {max_mortality} deaths")

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}

# categorize hurricanes in new dictionary with mortality severity as key
def mort_rating():
  mort_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for i in range(len(deaths)):
    for k, v in mortality_scale.items():
      if deaths[i] <= v:
        mort_dict[k] += [names[i], deaths[i]]
        break
      elif deaths[i] > 10000:
        mort_dict[5] += [names[i], deaths[i]]
        break
  return mort_dict
hurricanes_by_mortality = mort_rating()
#print(hurricanes_by_mortality)

# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
def costliest(ls):
  name = ""
  cost = 0.0
  for i in range(len(ls)):
    if ls[i] == 'Damages not recorded':
      continue
    elif float(ls[i]) > cost:
      cost = float(ls[i])
      name = names[i]
  return name, cost
max_damage_cane, max_damage = costliest(updated_damages)
#print(f"{max_damage_cane} cost ${max_damage}")

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def damage_rating():
  damage_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for i in range(len(updated_damages)):
    if updated_damages[i] == 'Damages not recorded':
      continue
    damage = float(updated_damages[i])
    for k, v in damage_scale.items():
      if damage <= v:
        damage_dict[k] += [names[i], damage]
        break
      elif damage > 50000000000:
        damage_dict[5] += [names[i], damage]
        break
  return damage_dict
hurricanes_by_damage = damage_rating()
#print(hurricanes_by_damage)