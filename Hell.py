from tkinter import *
from tkinter import messagebox
# functions

def Alc_Law_pop():
   messagebox.showinfo("Alcohol Law", "There is ample evidence that excessive consumption of alcohol can lead to health problems and even premature death. However, some people object to the state interfering in an individual's right to choose what he/she drinks. There is also the complication that the government can make a lot of money by taxing alcohol.")
def alc_tax_pop():
    messagebox.showinfo("Alcohol Tax", "Medically there is a clear case for the government to tax alcohol in order to discourage consumption because of its negative effects on health and its possible links to social breakdown. On the other hand, those who drink socially see the government benefiting from such a tax to be hypocritical.")
def Adult_edu_pop():
   messagebox.showinfo("Adult Eduation Subsidies", "Adult education subsidies are a way to encourage people to re-train and continue their education after they have joined the workforce. This includes evening classes and distance learning resources. These schemes help to raise the overall educational level of the workforce.")
def Agr_sub_pop():
   messagebox.showinfo("Agriculture Subsidies", "For strategic reasons some governments are happy to pay subsidies to farmers to ensure the security of the nation's food supply. This goes against free market economics and can also be very expensive, but it does safeguard jobs (and votes) in agricultural communities.")
# window creation
root =  Tk()
root.geometry("1280x720")
root.title("Democracy 3 Country Mod")
# fonts
Body = ("Arial",7)

Title = ("Arial Black", 10)
# label adding
c_detail = LabelFrame(root, text= "Country Details", font=Title)
c_detail.grid(row=0, column=0, sticky=N)

# country Details
c_name = Label(c_detail, text= "Country Name", font= Body)
c_name.grid(row=0,column=0, sticky=N)
c_name_box = Text(c_detail, width=15, height=1)
c_name_box.grid(row=0, column=1)

l_tit = Label(c_detail, text= "Leader Title", font= Body)
l_tit.grid(row=1, column=0)
l_tit_box = Text(c_detail, width=15, height=1)
l_tit_box.grid(row=1, column=1, padx=10)

pop = Label(c_detail, text= "Population (Million)", font= Body)
pop.grid(row=2,column=0, sticky=N)
pop_box = Text(c_detail, width=15, height=1)
pop_box.grid(row=2, column=1)

cur_sy = Label(c_detail, text= "Currency Symbol", font= Body)
cur_sy.grid(row=3, column= 0)
cur_sy_box = Text(c_detail, width=15, height=1)
cur_sy_box.grid(row=3, column=1)

max_gdp = Label(c_detail, text= "Max GDP (Millions)", font= Body)
max_gdp.grid(row=4, column=0)
max_gdp_box = Text(c_detail, width=15, height=1)
max_gdp_box.grid(row=4, column=1)

max_in = Label(c_detail, text= "Max Income (000)", font= Body)
max_in.grid(row=5, column=0)
max_in_box = Text(c_detail, width=15, height=1)
max_in_box.grid(row=5, column=1)

min_in = Label(c_detail, text= "Min Income (000)", font= Body)
min_in.grid(row=6, column=0)
min_in_box = Text(c_detail, width=15, height=1)
min_in_box.grid(row=6, column=1)

debt = Label(c_detail, text= "Debt (Millions)", font= Body)
debt.grid(row=7, column=0)
debt_box = Text(c_detail, width=15, height=1)
debt_box.grid(row=7, column=1)



help_label = LabelFrame(root, text="Click a policy for a brief description", font= Title)
help_label.grid(row=0, column=1, ipady=2)

#Alcohol Law

alc_law = Button(help_label, text = "Alcohol Law (1-6)",font=Body, command = Alc_Law_pop)
alc_law.grid(row=0, column=0)

choice_AlcLaw_sb = Spinbox(help_label, text="Alcohol law", from_=1, to=6)
choice_AlcLaw_sb.grid(row=0, column=1,)

#Alcohol Tax

alc_tax = Button(help_label, text = "Alcohol Tax (0-75%)",font=Body, command = alc_tax_pop)
alc_tax.grid(row=1, column=0)

choice_alctax_sb = Spinbox(help_label, text="Alcohol Tax", from_=0, to=75)
choice_alctax_sb.grid(row=1, column=1)

#AdultEducationSubsidies
Adult_edu = Button(help_label, text= "Adult Education Subsidies (0-4)",font=Body, command = Adult_edu_pop)
Adult_edu.grid(row=2, column=0)

Adult_edu_sb = Spinbox(help_label, text="Adult", from_=0, to=4)
Adult_edu_sb.grid(row=2, column=1)

#agriculture subsidies
Agr_sub = Button(help_label, text= "Agriculture Subsidies (0-4)",font=Body, command = Agr_sub_pop)
Agr_sub.grid(row=3, column=0)

Agr_sub_sb = Spinbox(help_label, text="Agriculture Subsidies", from_=0, to=4)
Agr_sub_sb.grid(row=3, column=1)

#Airline Tax
def Airline_Tax_pop():
   messagebox.showinfo("Airline Tax", "Airline fuel has generally not been subject to taxation. Supporters of air fuel taxes insist that this results in an unfair subsidy on an environmentally destructive form of transport. The airlines point out that taxing airline fuel will just encourage them to refuel elsewhere thereby diverting funds from our economy.")

Airline_tax = Button(help_label, text= "Airline Tax (0-75%)",font=Body, command = Airline_Tax_pop)
Airline_tax.grid(row=4, column=0)

Airline_tax_sb = Spinbox(help_label, text="Airline Tax", from_=0, to=75)
Airline_tax_sb.grid(row=4, column=1)

#Armed Police
def armed_police_pop():
   messagebox.showinfo("Armed police", "Arming police officers can be an effective strategy in deterring crime and maintaining order. Opponents would argue that it encourages criminals to use firearms in a 'criminal arms race'. Critics also worry that arming the police will distance them from law-abiding citizens.")

armed_police = Button(help_label, text= "Armed Police (0-4)",font=Body, command = armed_police_pop)
armed_police.grid(row=5, column=0)

armed_police_sb = Spinbox(help_label, text="Armed Police", from_=0, to=4)
armed_police_sb.grid(row=5, column=1)

# Ban Sunday Shopping
def ban_sunday_shopping_pop():
   messagebox.showinfo("Ban Sunday Shopping", "The Christian religion generally recognizes the 'Sabbath' as a 'day of rest' and many religious people believe that there should be no shopping carried out on that day. Some trade unions also believe that an enforced day of rest prevents its members being exploited.")
ban_sunday_shopping = Button(help_label, text= "Ban Sunday Shopping (0-4)",font=Body, command = ban_sunday_shopping_pop)
ban_sunday_shopping.grid(row=6, column=0)

ban_sunday_shopping_sb = Spinbox(help_label, text="Ban Sunday Shopping", from_=0, to=4)
ban_sunday_shopping_sb.grid(row=6, column=1)

#Biofuel Subsidies
def biofuel_subsidies_pop():
   messagebox.showinfo("Biofuel Subsidies", "Biofuels can reduce oil demand, by mixing ethanol derived from corn with petro-chemical fuel. This is generally popular with environmentalists. Farmers who earn money producing corn for biofuel use also benefit. Biofuels with a higher mix of ethanol can be subsidized through tax breaks.")

biofuel_subsidies = Button(help_label, text= "Biofuel Subsidies (0-4)",font=Body, command = biofuel_subsidies_pop)
biofuel_subsidies.grid(row=7, column=0)

biofuel_subsidies_sb = Spinbox(help_label, text="Biofuel Subsidies", from_=0, to=4)
biofuel_subsidies_sb.grid(row=7, column=1)

#Border Controls
def border_controls_pop():
   messagebox.showinfo("Border Controls", "Without some kind of customs checks at the borders, your country is open to the problem of mass illegal immigration. Some people argue that these immigrants cause crime, others that they take jobs away from your own citizens. Border controls can be effective in reducing illegal immigration.")
border_controls = Button(help_label, text= "Border Controls (1-5)",font=Body, command = border_controls_pop)
border_controls.grid(row=8, column=0)

border_controls_sb = Spinbox(help_label, text="Border Controls", from_=1, to=5)
border_controls_sb.grid(row=8, column=1)

#Bus lanes
def bus_lanes_pop():
   messagebox.showinfo("Bus Lanes", "Setting aside specific lanes of a road for use only by buses (and perhaps taxis and motorbikes) is one way to get traffic flowing faster and avoid congestion. It also shortens journey times for public transport and therefore encourages usage. There are noticeable costs involved in setting up such schemes, and motorists can be annoyed if the bus lanes seem empty while they remain stuck in traffic.")
bus_lanes = Button(help_label, text= "Bus Lanes (0-4)",font=Body, command = bus_lanes_pop)
bus_lanes.grid(row=9, column=0)

bus_lanes_sb = Spinbox(help_label, text="Bus Lanes", from_=0, to=4)
bus_lanes_sb.grid(row=9, column=1)

# Bus Subsidies 
def bus_subsidies_pop():
   messagebox.showinfo("Bus Subsidies", "Traffic congestion and pollution can be reduced by encouraging people to travel by bus instead of car. It can be an expensive option though, and some motorists may resent a transport system they do not use being subsidized.")
bus_subsidies = Button(help_label, text= "Bus Subsidies (0-4)",font=Body, command = bus_subsidies_pop)
bus_subsidies.grid(row=10, column=0)

bus_subsidies_sb = Spinbox(help_label, text="Bus Subsidies", from_=0, to=4)
bus_subsidies_sb.grid(row=10, column=1)

# Carbon Tax
def carbon_tax_pop():
   messagebox.showinfo("Carbon Tax", "A carbon tax is a tax levied on all emissions of Carbon Dioxide, thought to be the main cause of climate change. The tax is effectively a pollution tax, and a way to make those individuals and industries who contribute to climate change pay for the damage they cause or to reduce emissions. Obviously the tax is popular with environmentalists, and can also lead to a more energy efficient economy.")
carbon_tax = Button(help_label, text= "Carbon Tax (0-75%)",font=Body, command = carbon_tax_pop)
carbon_tax.grid(row=11, column=0)

carbon_tax_sb = Spinbox(help_label, text="Carbon Tax", from_=0, to=75)
carbon_tax_sb.grid(row=11, column=1)

# Car Emmission Limits
def car_emmission_limits_pop():
   messagebox.showinfo("Car Emmission Limits", "Setting legal limits on exhaust fumes helps to reduce air pollution, especially in cities, but it's unpopular with motorists who look upon it as yet more bureaucracy and tax.")
car_emmission_limits = Button(help_label, text= "Car Emmission Limits (0-4)",font=Body, command = car_emmission_limits_pop)
car_emmission_limits.grid(row=12, column=0)

car_emmission_limits_sb = Spinbox(help_label, text="Car Emmission Limits", from_=0, to=4)
car_emmission_limits_sb.grid(row=12, column=1)

# Car Tax
def car_tax_pop():
   messagebox.showinfo("Car Tax", "Taxing the ownership of all motor vehicles is one way to persuade people to use alternative forms of transport. It can be argued however, that such a  system increases the fixed costs of car ownership, encouraging people to use a car more once they have gone to the trouble of taxing it. There is also an argument that this is a tax that unfairly hits the poor and people in rural communities where a car is a necessity.")
car_tax = Button(help_label, text= "Car Tax (0-4)",font=Body, command = car_tax_pop)
car_tax.grid(row=13, column=0)

car_tax_sb = Spinbox(help_label, text="Car Tax", from_=0, to=4)
car_tax_sb.grid(row=13, column=1)

# CCTV Cameras
def cctv_cameras_pop():
   messagebox.showinfo("CCTV Cameras", "CCTV cameras can be a great help in catching criminals and cameras also deter crime.  The installation costs are extremely high, and there are concerns about civil rights from people who don't like to feel that the government is constantly watching them.")
cctv_cameras = Button(help_label, text= "CCTV Cameras (0-4)",font=Body, command = cctv_cameras_pop)
cctv_cameras.grid(row=14, column=0)

cctv_cameras_sb = Spinbox(help_label, text="CCTV Cameras", from_=0, to=4)
cctv_cameras_sb.grid(row=14, column=1)

# Child Benefits
def child_benefit_pop():
   messagebox.showinfo("Child Benefits", "A fixed payment made by the state directly to parents to assist in the cost of bringing up children. Popular with parents for obvious reasons, and the poor who see it as a redistributive tax, but capitalists are opposed to such an unnecessary level of interference by government. ")
child_benefit = Button(help_label, text= "Child Benefits (0-4)",font=Body, command = child_benefit_pop)
child_benefit.grid(row=15, column=0)

child_benefit_sb = Spinbox(help_label, text="Child Benefits", from_=0, to=4)
child_benefit_sb.grid(row=15, column=1)

# Childcare Provisions
def childcare_provisions_pop():
   messagebox.showinfo("Childcare Provisions", "By giving state subsidies for childcare, we can ensure more parents return to the workforce after having children, and therefore benefit the economy. Although this can be expensive, and is also a distortion of the market, it is popular with parents.")
childcare_provisions = Button(help_label, text= "Childcare Provisions (0-4)",font=Body, command = childcare_provisions_pop)
childcare_provisions.grid(row=16, column=0)

childcare_provisions_sb = Spinbox(help_label, text="Childcare Provisions", from_=0, to=4)
childcare_provisions_sb.grid(row=16, column=1)

# Citzenship Tests
def citizenship_tests_pop():
   messagebox.showinfo("Citizenship Tests", "Citizenship tests are a way of ensuring that people migrating to our country have a demonstrable understanding of our culture and history. This lessens the chances of a clash of cultures for newcomers to the country, encourages integration and reassures patriotic members of society that they need not fear immigration.")
citizenship_test = Button(help_label, text= "Citizenship Test (0-4)",font=Body, command = citizenship_tests_pop)
citizenship_test.grid(row=17, column=0)

citizenship_test_sb = Spinbox(help_label, text="Citizenship Test", from_=0, to=4)
citizenship_test_sb.grid(row=17, column=1)

#CleanEnergySubsidies
def clean_energy_subsidies_pop():
   messagebox.showinfo("Clean Energy Subsidies", "Renewable energy might not be ultra efficient yet, but there is an argument for investing heavily in it now so as to strategically prepare our country for a future without fossil fuels. Environmentalists are happy for obvious reasons, but capitalists see it as an unwelcome distortion of the energy market.")
clean_energy_subsidies = Button(help_label, text= "Clean Energy Subsidies (0-4)",font=Body, command = clean_energy_subsidies_pop)
clean_energy_subsidies.grid(row=18, column=0)

clean_energy_subsidies_sb = Spinbox(help_label, text="Clean Energy Subsidies", from_=0, to=4)
clean_energy_subsidies_sb.grid(row=18, column=1)

# clean fuel subsidy
def clean_fuel_subsidy_pop():
   messagebox.showinfo("Clean Fuel Subsidy", "A Subsidy for cleaner fuels such as Ultra-Low Sulfur fuel in an effort to reduce the environmental impact of motoring. The subsidy will reduce the costs of fitting catalytic converters to older cars, and provide an incentive at the  pump to choose less damaging fuels.")
clean_fuel_subsidy = Button(help_label, text= "Clean Fuel Subsidy (0-4)",font=Body, command = clean_fuel_subsidy_pop)
clean_fuel_subsidy.grid(row=19, column=0)

clean_fuel_subsidy_sb = Spinbox(help_label, text="Clean Fuel Subsidy", from_=0, to=4)
clean_fuel_subsidy_sb.grid(row=19, column=1)

# Community Policing 
def community_policing_pop():
   messagebox.showinfo("Communicating Policing", "Working with the community rather than attempting to control it. Community policing encourages the police to better understand the needs of the local community, especially in areas with ethnic minorities. Critics see it as an expensive waste of money which could be spent on more direct methods to cut crime.")
community_policing = Button(help_label, text= "Community Policing (0-4)",font=Body, command = community_policing_pop)
community_policing.grid(row=20, column=0)

community_policing_sb = Spinbox(help_label, text="Community Policing", from_=0, to=4)
community_policing_sb.grid(row=20, column=1)

# Consumer Rights
def consumer_rights_pop():
   messagebox.showinfo("Consumer Rights", "At a minimum level, the state guarantees that the consumer is not totally ripped off, at the other end of the spectrum, draconian legislation can benefit the consumer at the expense of business. Companies often complain about the amount of legislation governing selling to the public.")
consumer_rights = Button(help_label, text= "Consumer Rights (0-3)",font=Body, command = consumer_rights_pop)
consumer_rights.grid(row=21, column=0)

consumer_rights_sb = Spinbox(help_label, text="Consumer Rights", from_=0, to=3)
consumer_rights_sb.grid(row=21, column=1)

# Corporation Tax
def corporation_tax_pop():
   messagebox.showinfo("Corporation Tax", "A direct and proportionate tax on the profits of business. Some argue that this should be the only form of taxation, others that such taxes stifle entrepreneurship and discourage people from starting a business. It is often one of the main ways the government brings in money.")
corporation_tax = Button(help_label, text= "Corporation Tax (1-50%)",font=Body, command = corporation_tax_pop)
corporation_tax.grid(row=22, column=0)

corporation_tax_sb = Spinbox(help_label, text="Corporation Tax", from_=1, to=50)
corporation_tax_sb.grid(row=22, column=1)

# Creationism
def creationism_pop():
   messagebox.showinfo("Creationism", "A bitter battle has raged about the way children are taught evolution versus creationism. Scientists and Liberals consider it obvious that evidence based evolution should be taught in science classes. Some religious groups feel that it is wrong to teach evolution or 'Darwinism' as fact, when it remains an unproven theory or that creationism should be taught as an alternative theory in science. The government has to decide what is taught in our schools.")
creationism = Button(help_label, text= "Creationism (1-5)",font=Body, command = creationism_pop)
creationism.grid(row=23, column=0)

creationism_sb = Spinbox(help_label, text="Creationism", from_=1, to=5)
creationism_sb.grid(row=23, column=1)

# Curfews
def curfews_pop():
   messagebox.showinfo("Curfews", "Introduced  for a short period of time in  state of national emergency. These can be an effective way to combat crime at the cost of much personal liberty. Often, however, limiting the ability of peaceful citizens to leave their homes at night can be a sign of a country's degeneration into severe authoritarianism.")
curfews = Button(help_label, text= "Curfews (0-4)",font=Body, command = curfews_pop)
curfews.grid(row=24, column=0)

curfews_sb = Spinbox(help_label, text="Curfews", from_=0, to=4)
curfews_sb.grid(row=24, column=1)

# Death Penalty
def death_penalty_pop():
   messagebox.showinfo("Death Penalty", "The death penalty is the ultimate punishment for serious crimes. Opponents are concerned by the possibility of killing the wrong person, and suggest that only a barbaric state has the death penalty. Supporters point out that it absolutely guarantees no re-offending, and acts as a deterrent to serious crime.")
death_penalty = Button(help_label, text= "Death Penalty (0-5)",font=Body, command = death_penalty_pop)
death_penalty.grid(row=25, column=0)

death_penalty_sb = Spinbox(help_label, text="Death Penalty", from_=0, to=5)
death_penalty_sb.grid(row=25, column=1)

# Detention without trial
def detention_without_trial_pop():
   messagebox.showinfo("Dentention Without Trial", "Detention without trial allows your police and security services to detain suspects when they do not have sufficient evidence (or cannot reveal sensitive evidence) to convict suspects. This can be justified in the name of preventing terrorism, but Liberals are concerned that this infringes human-rights.")
detention_without_trial = Button(help_label, text= "Detention Without Trial (0-4)",font=Body, command = detention_without_trial_pop)
detention_without_trial.grid(row=26, column=0)

detention_without_trial_sb = Spinbox(help_label, text="Detention Without Trial", from_=0, to=4)
detention_without_trial_sb.grid(row=26, column=1)

# Disability Benefit
def disability_benefit_pop():
   messagebox.showinfo("Disability Benefit", "A direct payment from the state to disabled people to allow for the fact that they are possibly unable, or need assistance to work. Additionally many disabled people have special requirements in terms of transport or housing. ")
disability_benefit = Button(help_label, text= "Disability Benefit (0-4)",font=Body, command = disability_benefit_pop)
disability_benefit.grid(row=27, column=0)

disability_benefit_sb = Spinbox(help_label, text="Disability Benefit", from_=0, to=4)
disability_benefit_sb.grid(row=27, column=1)

# Faith School Subsidies
def faith_school_subsidies_pop():
   messagebox.showinfo("Faith School Subsidies", "Religious schools can achieve good academic standards. Their supporters make a case  that the government should subsidize methods of education that are proven to be effective. Critics say that religion has no place in education and that the government cannot be seen to 'push' a particular religion on children.")
faith_school_subsidies = Button(help_label, text= "Faith School Subsidies (0-4)",font=Body, command = faith_school_subsidies_pop)
faith_school_subsidies.grid(row=28, column=0)

faith_school_subsidies_sb = Spinbox(help_label, text="Faith School Subsidies", from_=0, to=4)
faith_school_subsidies_sb.grid(row=28, column=1)

# Foreign Aid
def foreign_aid_pop():
   messagebox.showinfo("Foreign Aid", "Some foreign countries have very poor economies, poor education or food shortages, and it can be argued that relatively rich nations such as ours have a moral duty to help them. Others may argue that the first priority of any nation is to its own citizens, and if those citizens wish to help, they can do so individually through charities.")
foreign_aid = Button(help_label, text= "Foreign Aid (0-4)",font=Body, command = foreign_aid_pop)
foreign_aid.grid(row=29, column=0)

foreign_aid_sb = Spinbox(help_label, text="Foreign Aid", from_=0, to=4)
foreign_aid_sb.grid(row=29, column=1)

# Free Bus Passes
def free_bus_passes_pop():
   messagebox.showinfo("Free Bus Passes", "Traditionally, free bus travel is offered as a concession to those citizens of retirement age. This can be expensive, but it’s a great way to reduce car usage and thus reduce pollution and congestion. Some oppose such a distortion of the market however.")
free_bus_passes = Button(help_label, text= "Free Bus Passes (0-4)",font=Body, command = free_bus_passes_pop)
free_bus_passes.grid(row=30, column=0)

free_bus_passes_sb = Spinbox(help_label, text="Free Bus Passes", from_=0, to=4)
free_bus_passes_sb.grid(row=30, column=1)

# Free Eye Tests
def free_eye_tests_pop():
   messagebox.showinfo("Free Eye Tests", "Eye tests catch problems early and advise those with poor eyesight that they need glasses. Getting your eyes tested privately can be expensive, and it's a luxury many people just do without. Socialists believe that the universal provision of free eye tests are essential in providing a health 'safety net' for all.")
free_eye_tests = Button(help_label, text= "Free Eye Tests (0-4)",font=Body, command = free_eye_tests_pop)
free_eye_tests.grid(row=31, column=0)

free_eye_tests_sb = Spinbox(help_label, text="Free Eye Tests", from_=0, to=4)
free_eye_tests_sb.grid(row=31, column=1)

# Free School Meals
def free_school_meals_pop():
   messagebox.showinfo("Free School Meals", "Not only are free school meals a way of redistributing wealth by ensuring everyone can afford to feed their children, its also a way to ensure that children eat healthily rather than surviving purely on junk food.")
free_school_meals = Button(help_label, text= "Free School Meals (0-4)",font=Body, command = free_school_meals_pop)
free_school_meals.grid(row=32, column=0)

free_school_meals_sb = Spinbox(help_label, text="Foreign Aid", from_=0, to=4)
free_school_meals_sb.grid(row=32, column=1)

# Gambling
def gambling_pop():
   messagebox.showinfo("Gambling", "To some, gambling is a sin which leads to poverty and disaster, but others believe that some 'social' gambling is harmless fun which can also be taxed nicely by the government as an additional form of revenue. It also encourages tourism and creates jobs.")
gambling = Button(help_label, text= "Gambling (0-2)",font=Body, command = gambling_pop)
gambling.grid(row=33, column=0)

gambling_sb = Spinbox(help_label, text="Gambling", from_=0, to=2)
gambling_sb.grid(row=33, column=1)

# Gated communities
def gated_communities_pop():
   messagebox.showinfo("Gated Communities", "A drastic solution to serious street crime and vandalism, gated communities are basically self-policed residential areas. They are popular with the wealthy, but often associated with class divide and inequality, as only the relatively wealthy can afford to live inside them. As a result, some governments are reluctant to permit their construction.")
gated_communities = Button(help_label, text= "Gated Communities (0-2)",font=Body, command = gated_communities_pop)
gated_communities.grid(row=34, column=0)

gated_communities_sb = Spinbox(help_label, text="Gated Communities", from_=0, to=2)
gated_communities_sb.grid(row=34, column=1)

# Graduate Tax
def graduate_tax_pop():
   messagebox.showinfo("Graduate Tax", "A graduate tax is a deciated tax levied purely on people graduating from university, as a way of them contributing to the cost of their university tuition. Supporters say this is fair because not everyone benefits from a university education. Opponents argue that it creates a disincentive to study purely academic subjects and the arts, as well as penalizing ambition.")
graduate_tax = Button(help_label, text= "Graduate Tax (0-4)",font=Body, command = graduate_tax_pop)
graduate_tax.grid(row=35, column=0)

graduate_tax_sb = Spinbox(help_label, text="Graduate Tax", from_=0, to=4)
graduate_tax_sb.grid(row=35, column=1)

# Handgun Laws
def handgun_laws_pop():
   messagebox.showinfo("Handgun Laws", "Some countries allow the virtually unrestricted ownership of any kind of firearm, whereas in others it is strictly controlled. Some people talk of the basic right to defend yourself, others are concerned that gun ownership leads to gun crime.")
handgun_laws = Button(help_label, text= "Handguns Laws (1-7)",font=Body, command = handgun_laws_pop)
handgun_laws.grid(row=36, column=0)

handgun_laws_sb = Spinbox(help_label, text="Handgun Laws", from_=1, to=7)
handgun_laws_sb.grid(row=36, column=1)

# Hydrid Cars Initiative
def hybrid_cars_initiative_pop():
   messagebox.showinfo("Hybrid Cars Initiative", "Hybrid cars are less damaging to the environment, because at slower speeds they use electric engines that produce no CO2. They also get higher fuel efficiency, thus reducing demand for oil. The downside is they are very expensive, but tax incentives can encourage more people to buy hybrid models when they get new cars.")
hybrid_cars_initiative = Button(help_label, text= "Hybrid Cars Initiative (0-4)",font=Body, command = hybrid_cars_initiative_pop)
hybrid_cars_initiative.grid(row=0, column=2)

hybrid_cars_initiative_sb = Spinbox(help_label, text="Hybrid Cars Initiative", from_=0, to=4)
hybrid_cars_initiative_sb.grid(row=0, column=3)

#ID cards
def id_cards_pop():
   messagebox.showinfo("ID Cards", "Some say ID Cards act as a powerful deterrent against terrorism and other serious crimes, but liberals would argue that it is an infringement of an individual's civil liberties for the state to demand that citizens identify themselves on the spot.")
id_cards = Button(help_label, text= "ID Cards (0-4)",font=Body, command = id_cards_pop)
id_cards.grid(row=1, column=2)

id_cards_sb = Spinbox(help_label, text="ID Cards", from_=0, to=4)
id_cards_sb.grid(row=1, column=3)

#Import tariffs
def import_tariffs_pop():
   messagebox.showinfo("Import Tariffs", "Cheap imports can be damaging to the economy because local companies cannot match the lower salaries paid by foreign competitors. Import tariffs help to protect local manufacturers from 'unfair' competition. This does go against real free-market economics though, and can be seen as being unfair to foreign countries, possibly sparking retaliation.")
import_tariffs = Button(help_label, text= "Import Tariffs (0-4)",font=Body, command = import_tariffs_pop)
import_tariffs.grid(row=2, column=2)

import_tariffs_sb = Spinbox(help_label, text="Import Tariffs", from_=0, to=4)
import_tariffs_sb.grid(row=2, column=3)

# Income Tax
def income_tax_pop():
   messagebox.showinfo("Income Tax", "One of the most popular ways to raise money for government is a direct tax on peoples earnings, deducted at source by their employer. Income tax is generally a progressive tax (the wealthy pay more as a fraction of their income than the poor) and for this reason it is popular with socialists and the low paid.")
income_tax = Button(help_label, text= "Income Tax (1-90%)",font=Body, command = income_tax_pop)
income_tax.grid(row=3, column=2)

income_tax_sb = Spinbox(help_label, text="Income Tax", from_=1, to=90)
income_tax_sb.grid(row=3, column=3)

# Flat Tax
def flat_tax_pop():
   messagebox.showinfo("Flat Tax", "A flat-rate income tax is a tax where every citizen pays the same marginal rate of income tax regardless of their total income. As a result, the cleaner in the office pays the same rate as the CEO, though the CEO's total tax bill will be higher. This simpler structure can lead to lower avoidance and evasion. It is not progressive, and can exacerbate income inequality.")
flat_tax = Button(help_label, text= "Flat Tax (1-90)",font=Body, command = flat_tax_pop)
flat_tax.grid(row=4, column=2)

flat_tax_sb = Spinbox(help_label, text="Flat Tax", from_=1, to=90)
flat_tax_sb.grid(row=4, column=3)

# Capital Gains Tax
def capital_gains_tax_pop():
   messagebox.showinfo("Capital Gains Tax", "CGT is a tax levied on non-salary income such as stock market profits and share dividends, and profits from selling property or other assets. Primarily it affects the wealthy and business owners, and will raise more money if the economy is booming. Because it taxes profits from investments, it also acts as a slight deterrent to investment and thus be detrimental to the economy.")
capital_gains_tax = Button(help_label, text= "Capital Gains Tax (1-50%)",font=Body, command = capital_gains_tax_pop)
capital_gains_tax.grid(row=5, column=2)

capital_gains_tax_sb = Spinbox(help_label, text="Capital Gains Tax", from_=1, to=50)
capital_gains_tax_sb.grid(row=5, column=3)

# Inheritance Tax
def inheritance_tax_pop():
   messagebox.showinfo("Inheritance Tax", "A tax paid on the wealth of an individual as it is passed on to their descendants. An inheritance tax protects equality, by preventing families amassing wealth and advantage over the generations, so it is popular with socialists and the poor. However, some people are strongly opposed to anything that prevents them handing on their hard-earned wealth, especially their house, to their children.")
inheritance_tax = Button(help_label, text= "Inheritance Tax (1-75%)",font=Body, command = inheritance_tax_pop)
inheritance_tax.grid(row=6, column=2)

inheritance_tax_sb = Spinbox(help_label, text="Inheritance Tax", from_=1, to=75)
inheritance_tax_sb.grid(row=6, column=3)

# intelligence_services
def intelligence_services_pop():
   messagebox.showinfo("Intelligence Services", "Security services are an essential tool in the fight against organized crime and terrorism. Good, reliable intelligence can be difficult and expensive to obtain, and in many cases the methods employed can be unpopular with liberals and human rights advocates.")
intelligence_services = Button(help_label, text= "Intelligence Services (1-5)",font=Body, command = intelligence_services_pop)
intelligence_services.grid(row=7, column=2)

intelligence_services_sb = Spinbox(help_label, text="Intelligence Services", from_=1, to=5)
intelligence_services_sb.grid(row=7, column=3)

# internet_censorship
def internet_censorship_pop():
   messagebox.showinfo("Internet Censorship", "Liberals would suggest that the internet's greatest characteristic is its freedom from censorship and control, leading to an open and tolerant society. Freedom has its price however, and there is no shortage of material on the internet that can assist those with criminal intent. Opinion on what should and should not be censored on the web is bitterly divided.")
internet_censorship = Button(help_label, text= "Internet Censorship (0-3)",font=Body, command = internet_censorship_pop)
internet_censorship.grid(row=8, column=2)

internet_censorship_sb = Spinbox(help_label, text="Internet Censorship", from_=0, to=3)
internet_censorship_sb.grid(row=8, column=3)

# internet_tax
def internet_tax_pop():
   messagebox.showinfo("Internet Tax", "As more and more commerce moves from conventional 'bricks and mortar' establishments to the web, governments are tempted to levy taxes on such transactions in order to 'level the playing field'. However, opponents of an internet tax claim that such a move would cripple the hi-tech economy and do enormous harm to the country's competitiveness.")
internet_tax = Button(help_label, text= "Internet Tax (0-75%)",font=Body, command = internet_tax_pop)
internet_tax.grid(row=9, column=2)

internet_tax_sb = Spinbox(help_label, text="Internet Tax", from_=0, to=75)
internet_tax_sb.grid(row=9, column=3)

# jury_trial
def jury_trial_pop():
   messagebox.showinfo("Jury Trial", "The right to be tried by ordinary members of the public rather than a judge is seen as a fundamental human right by many liberals. Conservatives argue that such a process is expensive, time wasting and is no fairer than a judge or a group of magistrates. Its entirely possible to have a system where a jury trial is reserved for more serious offences, with minor trials presided over by a magistrate.")
jury_trial = Button(help_label, text= "Jury Trial (0-4)",font=Body, command = jury_trial_pop)
jury_trial.grid(row=10, column=2)

jury_trial_sb = Spinbox(help_label, text="Jury Trial", from_=0, to=4)
jury_trial_sb.grid(row=10, column=3)

# labour_laws
def labour_laws_pop():
   messagebox.showinfo("Labour Laws", "Labor laws are basically restrictions on a worker's right to strike. Capitalists argue that such restrictions are vital to prevent key workers such as power station workers, policemen and train drivers from holding the country to ransom. Trade unionists consider the right to strike to be fundamental and not open to negotiation.")
labour_laws = Button(help_label, text= "Labour Laws (1-3)",font=Body, command = labour_laws_pop)
labour_laws.grid(row=11, column=2)

labour_laws_sb = Spinbox(help_label, text="Labour Laws", from_=1, to=3)
labour_laws_sb.grid(row=11, column=3)

# legal_aid
def legal_aid_pop():
   messagebox.showinfo("Legal Aid", "Not everyone has the money to pay a lawyer to defend themselves in court. Although a citizen could theoretically defend himself, providing state-employed lawyers should make for a fairer system. On the other hand, this is basically a big subsidy to people who have already been charged with a crime but remember they are innocent until proved guilty.")
legal_aid = Button(help_label, text= "Legal Aid",font=Body, command = legal_aid_pop)
legal_aid.grid(row=12, column=2)

legal_aid_sb = Spinbox(help_label, text="Legal Aid", from_=0, to=5)
legal_aid_sb.grid(row=12, column=3)

# legalise_prostitution
def legalise_prostitution_pop():
   messagebox.showinfo("Legalise Prostitution", "Conservatives claim that the legalization of prostitution would mark a severe decline in family values. Others claim that as prostitution is unlikely to disappear, even if illegal, it's better for society and prostitutes that the practice is regulated and monitored rather than criminalized.")
legalise_prostitution = Button(help_label, text= "Legalise Prostitution",font=Body, command = legalise_prostitution_pop)
legalise_prostitution.grid(row=12, column=2)

legalise_prostitution_sb = Spinbox(help_label, text="Legalise Prostitution", from_=0, to=5)
legalise_prostitution_sb.grid(row=12, column=3)

# luxury_goods_tax
def luxury_goods_tax_pop():
   messagebox.showinfo("Luxury Goods Tax", "A tax aimed specifically at the high spenders in our society. A surcharge is added to high value luxuries such as sports cars, private yachts etc. Although it is never a vast source of income, a luxury goods tax can be popular with those people concerned with the gap between rich and poor. A luxury goods tax could encourage high earners to live and work elsewhere.")
luxury_goods_tax = Button(help_label, text= "Luxury Goods Tax",font=Body, command = luxury_goods_tax_pop)
luxury_goods_tax.grid(row=13, column=2)

luxury_goods_tax_sb = Spinbox(help_label, text="Luxury Goods Tax", from_=0, to=5)
luxury_goods_tax_sb.grid(row=13, column=3)

# married_tax_allowance
def married_tax_allowance_pop():
   messagebox.showinfo("Married Tax Allowance", "This is a tax break for married couples, given as an encouragement for people to marry and also to stick together. Church groups see it as essential that the state encourages traditional family values. Some see it as religion meddling in the tax system for no good reason.")
married_tax_allowance = Button(help_label, text= "Married Tax Allowance",font=Body, command = married_tax_allowance_pop)
married_tax_allowance.grid(row=13, column=2)

married_tax_allowance_sb = Spinbox(help_label, text="Married Tax Allowance", from_=0, to=5)
married_tax_allowance_sb.grid(row=13, column=3)

# maternity_leave
def maternity_leave_pop():
   messagebox.showinfo("Maternity Leave", "To some people, ensuring that mothers have a right to maternity leave and to return to their jobs afterwards is a sign of a civilized society, and one that encourages women to work. Some small businesses are concerned that it can put an unpredictable and even potentially crippling burden on an employer, especially where the number of employees is small. It could be argued that this actually encourages employers not to employ women.")
maternity_leave = Button(help_label, text= "Maternity Leave",font=Body, command = maternity_leave_pop)
maternity_leave.grid(row=14, column=2)

maternity_leave_sb = Spinbox(help_label, text="Maternity Leave", from_=0, to=5)
maternity_leave_sb.grid(row=14, column=3)

# microgeneration_grants
def microgeneration_grants_pop():
   messagebox.showinfo("Microgeneration Grants", "These grants are given to citizens to help subsidize the cost of energy micro-generation systems such as solar panels and wind turbines. This is a good way to take advantage of some people's desire to make a personal step towards cleaner and greener energy, and will increase the country's overall energy efficiency.")
microgeneration_grants = Button(help_label, text= "Microgeneration Grants",font=Body, command = microgeneration_grants_pop)
microgeneration_grants.grid(row=15, column=2)

microgeneration_grants_sb = Spinbox(help_label, text="Microgeneration Grants", from_=0, to=5)
microgeneration_grants_sb.grid(row=15, column=3)

#  military_spending
def military_spending_pop():
   messagebox.showinfo("Military Spending", "A modern, well equipped military can cost an absolute fortune, and many people feel that the money could best be spent elsewhere. Others (especially patriots) would argue that you cannot put a price on freedom and security, and also point out the huge benefits for our businesses, technology and employment figures.")
military_spending = Button(help_label, text= "Military Spending",font=Body, command = military_spending_pop)
military_spending.grid(row=16, column=2)

military_spending_sb = Spinbox(help_label, text="Military Spending", from_=0, to=5)
military_spending_sb.grid(row=16, column=3)

# monorail
def monorail_pop():
   messagebox.showinfo("Monorail", "Monorails are often seen as the transport system of the future. They are promoted as being fast, reliable and environmentally beneficial. The main problem however is the high cost. The construction time is also a major consideration so investment in a national network would take a long time to give an eventually good payoff.")
monorail = Button(help_label, text= "Monorail",font=Body, command = monorail_pop)
monorail.grid(row=17, column=2)

monorail_sb = Spinbox(help_label, text="Monorail", from_=0, to=5)
monorail_sb.grid(row=17, column=3)

# mortgage_tax_relief
def mortgage_tax_relief_pop():
   messagebox.showinfo("Mortgage Tax Relief", "This allows people to claim tax relief on the interest payments they have to make when they borrow money to buy a house. This helps homebuyers to afford their mortgage payments, but can be resented by those who are not in a position to buy a house, as it is effectively a tax break for homebuyers.")
mortgage_tax_relief = Button(help_label, text= "Mortgage Tax Relief",font=Body, command = mortgage_tax_relief_pop)
mortgage_tax_relief.grid(row=18, column=2)

mortgage_tax_relief_sb = Spinbox(help_label, text="Mortgage Tax Relief", from_=0, to=5)
mortgage_tax_relief_sb.grid(row=18, column=3)

# narcotics
def narcotics_pop():
   messagebox.showinfo("Narcotics", "Should drugs such as cannabis and heroin be legalized? Supporters suggest that it is the crime associated with the buying black-market drugs that cause problems, and legalizing narcotics would reduce crime. Opponents point to the health risks and say it would be giving into criminals.")
narcotics = Button(help_label, text= "Narcotics",font=Body, command = narcotics_pop)
narcotics.grid(row=19, column=2)

narcotics_sb = Spinbox(help_label, text="Narcotics", from_=0, to=5)
narcotics_sb.grid(row=19, column=3)

# national_service
def national_service_pop():
   messagebox.showinfo("National Service", "Compulsory military service for some citizens where they are taught the basics of how to defend this country from attack has some benefits. For example it would allow us to have a smaller regular army. However, there are concerns about forcing people to bear arms against their will.")
national_service = Button(help_label, text= "National Service",font=Body, command = national_service_pop)
national_service.grid(row=20, column=2)

national_service_sb = Spinbox(help_label, text="National Service", from_=0, to=5)
national_service_sb.grid(row=20, column=3)

# organ_donation
def organ_donation_pop():
   messagebox.showinfo("Organ Donation", "There are few who would disagree that organ transplant is an amazing technology but it requires a plentiful supply of donors. Sadly many people do not give the topic consideration. Some suggest that an 'opt-out' policy is best, with consent for donation assumed unless otherwise stated. Others suggest that this is no place for the state to interfere and explicit permission should be requested.")
organ_donation = Button(help_label, text= "Organ Donation",font=Body, command = organ_donation_pop)
organ_donation.grid(row=21, column=2)

organ_donation_sb = Spinbox(help_label, text="Organ Donation", from_=0, to=5)
organ_donation_sb.grid(row=21, column=3)

# organic_subsidy
def organic_subsidy_pop():
   messagebox.showinfo("Organic Subsidy", "Supporters of organic farming say the state should subsidize this method of farming because of the perceived health benefits of food without artificial flavorings and additives. Naturally this is popular with farmers and environmentalists, but some people see it as a pointless distortion of what should be a free market.")
organic_subsidy = Button(help_label, text= "Organic Subsidy",font=Body, command = organic_subsidy_pop)
organic_subsidy.grid(row=22, column=2)

organic_subsidy_sb = Spinbox(help_label, text="Organic Subsidy", from_=0, to=5)
organic_subsidy_sb.grid(row=22, column=3)

# petrol_tax
def petrol_tax_pop():
   messagebox.showinfo("Petrol Tax", "Taxing fuel can be a huge source of income for a government, and can also be seen as a 'green' policy by encouraging people to drive less, or to use more fuel efficient cars. Critics suggest that this is just another cynical tax on the motorist, and some complain that the alternative (public transport) is not a viable option for everyone.")
petrol_tax = Button(help_label, text= "Petrol Tax",font=Body, command = petrol_tax_pop)
petrol_tax.grid(row=23, column=2)

petrol_tax_sb = Spinbox(help_label, text="Petrol Tax", from_=0, to=5)
petrol_tax_sb.grid(row=23, column=3)

# phone_tapping
def phone_tapping_pop():
   messagebox.showinfo("Phone Tapping", "From a law and order perspective, wire tapping is an essential weapon in the fight against organized crime and terrorism. The problem is that it's difficult to prevent misuse of such a system, and liberals are keen to point out how widespread wire tapping is a very sinister sign of a police state.")
phone_tapping = Button(help_label, text= "Phone Tapping",font=Body, command = phone_tapping_pop)
phone_tapping.grid(row=24, column=2)

phone_tapping_sb = Spinbox(help_label, text="Phone Tapping", from_=0, to=5)
phone_tapping_sb.grid(row=24, column=3)

# plastic_bag_tax
def plastic_bag_tax_pop():
   messagebox.showinfo("Plastic Bag Tax", "Plastic bags, unlike paper ones are not biodegradable so can last more or less forever, eventually ending up in huge unsightly landfill sites. A tax on bags discourages their use and encourages people to re-use stronger, more environmentally friendly alternatives. Capitalists just see this as the state meddling.")
plastic_bag_tax = Button(help_label, text= "Plastic Bag Tax",font=Body, command = plastic_bag_tax_pop)
plastic_bag_tax.grid(row=25, column=2)

plastic_bag_tax_sb = Spinbox(help_label, text="Plastic Bag Tax", from_=0, to=5)
plastic_bag_tax_sb.grid(row=25, column=3)

# police_force
def police_force_pop():
   messagebox.showinfo("Police Force", "Every government needs to employ a police force to ensure order is kept and laws are obeyed, but it's a matter of debate exactly how much should be spent on the police. Some favor a large force with police on every street corner, other prefer a more low-key and tolerant approach.")
police_force = Button(help_label, text= "Police Force",font=Body, command = police_force_pop)
police_force.grid(row=26, column=2)

police_force_sb = Spinbox(help_label, text="Police Force", from_=0, to=5)
police_force_sb.grid(row=26, column=3)

# pollution_controls
def pollution_controls_pop():
   messagebox.showinfo("Pollution Controls", "Restrictions on what chemicals and emissions can be released into the atmosphere. Controls reduce pollution and increase health, possibly at the cost of economic competitiveness.")
pollution_controls = Button(help_label, text= "Pollution Controls",font=Body, command = pollution_controls_pop)
pollution_controls.grid(row=27, column=2)

pollution_controls_sb = Spinbox(help_label, text="Pollution Controls", from_=0, to=5)
pollution_controls_sb.grid(row=27, column=3)

# prison_tagging
def prison_tagging_pop():
   messagebox.showinfo("Prison Tagging", "A high tech alternative to incarceration that allows people to re-integrate with the community upon release from prison, whilst allowing law enforcement authorities to keep a close eye on them. Liberals have concerns that such a system is a step towards a police state which monitors our every move.")
prison_tagging = Button(help_label, text= "Prison Tagging",font=Body, command = prison_tagging_pop)
prison_tagging.grid(row=28, column=2)

prison_tagging_sb = Spinbox(help_label, text="Prison Tagging", from_=0, to=5)
prison_tagging_sb.grid(row=28, column=3)

# prisons
def prisons_pop():
   messagebox.showinfo("Prisons", "Some argue that providing the minimum number of bare, cold cells is the only provision that needs to be made for those who have broken the law. Others suggest that spending more money allows for prisoners to be rehabilitated as well as punished and reduces the chances of reoffending.")
prisons = Button(help_label, text= "Prisons",font=Body, command = prisons_pop)
prisons.grid(row=29, column=2)

prisons_sb = Spinbox(help_label, text="Prisons", from_=0, to=5)
prisons_sb.grid(row=29, column=3)

# property_tax
def property_tax_pop():
   messagebox.showinfo("Property Tax", "Property tax is a tax levied on the value of homes. The valuation is often made by a government body, and the money is used to fund local government services (at least in part) such as the provision of street lighting and emergency services. Some see it as a fair tax which mostly affects those who own large homes and are wealthy, others see it as an unfair tax on retired people with large homes but little actual income.")
property_tax = Button(help_label, text= "Property Tax",font=Body, command = property_tax_pop)
property_tax.grid(row=30, column=2)

property_tax_sb = Spinbox(help_label, text="Property Tax", from_=0, to=5)
property_tax_sb.grid(row=30, column=3)

# public_libraries
def public_libraries_pop():
   messagebox.showinfo("Public Libraries", "Public libraries provide a number of services, acting as a focus for communities, providing access to information and literature to those on low incomes, and enabling people to learn new skills outside the normal educational establishment.")
public_libraries = Button(help_label, text= "Public Libraries",font=Body, command = public_libraries_pop)
public_libraries.grid(row=31, column=2)

public_libraries_sb = Spinbox(help_label, text="Public Libraries", from_=0, to=5)
public_libraries_sb.grid(row=31, column=3)

# racial_profiling
def racial_profiling_pop():
   messagebox.showinfo("Racial Profiling", "Racial (or ethnic) profiling is the practice of using race as a factor in identifying criminals and potential criminals. Law enforcement officials claim that using racial profiling allows them to quickly narrow down lists of potential suspects, and to best concentrate their efforts but opponents fear that it leads to racial discrimination by the police.")
racial_profiling = Button(help_label, text= "Racial Profiling",font=Body, command = racial_profiling_pop)
racial_profiling.grid(row=32, column=2)

racial_profiling_sb = Spinbox(help_label, text="Racial Profiling", from_=0, to=5)
racial_profiling_sb.grid(row=32, column=3)

# race_discrimination_act
def race_discrimination_act_pop():
   messagebox.showinfo("Race Discrimination Act", "Prevents citizens being discriminated against purely on the basis of race, i.e. racist employment practices etc.")
race_discrimination_act = Button(help_label, text= "Race Discrimination Act",font=Body, command = race_discrimination_act_pop)
race_discrimination_act.grid(row=33, column=2)

race_discrimination_act_sb = Spinbox(help_label, text="Race Discrimination Act", from_=0, to=5)
race_discrimination_act_sb.grid(row=33, column=3)

# rail_subsidies
def rail_subsidies_pop():
   messagebox.showinfo("Rail Subsidies", "Travelling by rail is not only more environmentally sound than car travel, its much more efficient in terms of transport times and congestion. Of course that requires adequate investment over the very long term, and in the meantime, motorists take offence at subsidizing a system they do not use. It can take several years for the effects of rail investment to take effect.")
rail_subsidies = Button(help_label, text= "Rail Subsidies",font=Body, command = rail_subsidies_pop)
rail_subsidies.grid(row=34, column=2)

rail_subsidies_sb = Spinbox(help_label, text="Rail Subsidies", from_=0, to=5)
rail_subsidies_sb.grid(row=34, column=3)

# recycling
def recycling_pop():
   messagebox.showinfo("Recycling", "Supporters of recycling argue that dumping waste in landfills just isn't a long term solution, and the government needs to show the way by providing facilities to recycle as many waste materials as possible. This might include recycling newspapers, cardboard, bottles and even some plastics.")
recycling = Button(help_label, text= "Recycling",font=Body, command = recycling_pop)
recycling.grid(row=35, column=2)

recycling_sb = Spinbox(help_label, text="Recycling", from_=0, to=5)
recycling_sb.grid(row=35, column=3)

# road_building
def road_building_pop():
   messagebox.showinfo("Road Building", "Although environmentalists often argue that more roads just lead to more congestion, not surprisingly this isn't how the motorist who is sat in traffic sees it. Building new roads is a very expensive and very slow process, but some suggest its vital to keep our economy functioning.")
road_building = Button(help_label, text= "Road Building",font=Body, command = road_building_pop)
road_building.grid(row=36, column=2)

road_building_sb = Spinbox(help_label, text="Road Building", from_=0, to=5)
road_building_sb.grid(row=36, column=3)

# rural_development_grants
def rural_development_grants_pop():
   messagebox.showinfo("Rural Development Grants", "As technology advances and more and more citizens take jobs in our cities, there is a danger that poverty and unemployment will rise to unacceptable levels in the countryside. Rural development grants do distort the free market, but they also support rural businesses and prevent poverty amongst farmers and other rural occupations.")
rural_development_grants = Button(help_label, text= "Rural Development Grants",font=Body, command = rural_development_grants_pop)
rural_development_grants.grid(row=0, column=4)

rural_development_grants_sb = Spinbox(help_label, text="Rural Development Grants", from_=0, to=5)
rural_development_grants_sb.grid(row=0, column=5)

# sales_tax
def sales_tax_pop():
   messagebox.showinfo("Sales Tax", "Sales tax is the classic 'regressive' tax, which means it does not take into account the ability to pay. Critics argue that this affects the poor disproportionately and thus increases inequality. Supporters argue that it is relatively easy to collect and affects everyone, and is thus fair. Businesses can be opposed to the administrative burden of the tax.")
sales_tax = Button(help_label, text= "Sales Tax",font=Body, command = sales_tax_pop)
sales_tax.grid(row=1, column=4)

sales_tax_sb = Spinbox(help_label, text="Sales Tax", from_=0, to=5)
sales_tax_sb.grid(row=1, column=5)

# satelite_road_pricing
def satelite_road_pricing_pop():
   messagebox.showinfo("Satelite Road Pricing", "An expensive system that requires transponders to be fitted to everyone's car and keeps track of what roads people use (and when). Allows per-road pricing for car usage which gives local authorities fine control over reducing congestion without burdening motorists in more remote rural areas who have no alternative transport system.")
satelite_road_pricing = Button(help_label, text= "Satelite Road Pricing",font=Body, command = satelite_road_pricing_pop)
satelite_road_pricing.grid(row=2, column=4)

satelite_road_pricing_sb = Spinbox(help_label, text="Satelite Road Pricing", from_=0, to=5)
satelite_road_pricing_sb.grid(row=2, column=5)

# school_buses
def school_buses_pop():
   messagebox.showinfo("School Buses", "State subsidies for school buses ensure that every school kid has an efficient, and safe journey to school, whilst reducing the number of short 'school-run' trips carried out by parents, thus reducing traffic on the roads. Parents are also happier knowing that there are proper approved school buses.")
school_buses = Button(help_label, text= "School Buses",font=Body, command = school_buses_pop)
school_buses.grid(row=3, column=4)

school_buses_sb = Spinbox(help_label, text="School Buses", from_=0, to=5)
school_buses_sb.grid(row=3, column=5)

# school_prayers
def school_prayers_pop():
   messagebox.showinfo("School Prayers", "Liberals will often argue that the education of our younger citizens should be kept entirely separate from any religious teachings. On the other hand, it's argued that some compulsory prayer in schools is a way of promoting moral values in our children.")
school_prayers = Button(help_label, text= "School Prayers",font=Body, command = school_prayers_pop)
school_prayers.grid(row=4, column=4)

school_prayers_sb = Spinbox(help_label, text="School Prayers", from_=0, to=5)
school_prayers_sb.grid(row=4, column=5)

# science_funding
def science_funding_pop():
   messagebox.showinfo("Science Funding", "In some countries, the majority of research is funded by private companies. State-sponsored science can be useful for investing in very long-term research projects or those that may not be commercially rewarding. The benefits of state sector research are freely available to the entire population, rather than patented by corporations.")
science_funding = Button(help_label, text= "Science Funding",font=Body, command = science_funding_pop)
science_funding.grid(row=5, column=4)

science_funding_sb = Spinbox(help_label, text="Science Funding", from_=0, to=5)
science_funding_sb.grid(row=5, column=5)

# small_business_grants
def small_business_grants_pop():
   messagebox.showinfo("Small Business Grants", "The failure rate for small businesses is very high. In the early years of trading, a preferential government grant can be an enormous help to get a new enterprise off the ground. This can lead to a big boost to the economy, but it can also be an expensive policy with no guarantee of good results.")
small_business_grants = Button(help_label, text= "Small Business Grants",font=Body, command = small_business_grants_pop)
small_business_grants.grid(row=6, column=4)

small_business_grants_sb = Spinbox(help_label, text="Small Business Grants", from_=0, to=5)
small_business_grants_sb.grid(row=6, column=5)

# space_program
def space_program_pop():
   messagebox.showinfo("Space Program", "Invest in your country's efforts to explore space! As well as the purely scientific benefits, a well-funded space program will boost the level of technological expertise throughout the entire economy. It will also unite the country and encourage patriotism.")
space_program = Button(help_label, text= "Space Program",font=Body, command = space_program_pop)
space_program.grid(row=7, column=4)

space_program_sb = Spinbox(help_label, text="Space Program", from_=0, to=5)
space_program_sb.grid(row=7, column=5)

# speed_cameras
def speed_cameras_pop():
   messagebox.showinfo("Speed Cameras", "Speed cameras are an automated way to enforce speed restrictions on our roads, without having to invest a fortune in extra traffic police. Supporters claim they reduce road deaths and free up the police to deal with more serious crime, opponents claim they are a cynical way of taxing the motorist and have nothing to do with safety")
speed_cameras = Button(help_label, text= "Speed Cameras",font=Body, command = speed_cameras_pop)
speed_cameras.grid(row=8, column=4)

speed_cameras_sb = Spinbox(help_label, text="Speed Cameras", from_=0, to=5)
speed_cameras_sb.grid(row=8, column=5)

# state_health_service
def state_health_service_pop():
   messagebox.showinfo("State Health Service", "Although many citizens would be happy to pay privately for their own health treatment, there is an argument that the state has a duty to provide a minimum level of free health treatment for everyone regardless of income. Health provision can be expensive, so it's a matter of debate as to how much should be spent.")
state_health_service = Button(help_label, text= "State Health Service",font=Body, command = state_health_service_pop)
state_health_service.grid(row=9, column=4)

state_health_service_sb = Spinbox(help_label, text="State Health Service", from_=0, to=5)
state_health_service_sb.grid(row=9, column=5)

# state_housing
def state_housing_pop():
   messagebox.showinfo("State Housing", "Some citizens prefer to own their own homes, but the cost of housing is such that a large proportion of the population live in rented accommodation. State housing is provided, at a reduced rate, to those who cannot afford to pay the market rate. This can be expensive to fund, but the social benefits are also significant.")
state_housing = Button(help_label, text= "State Housing",font=Body, command = state_housing_pop)
state_housing.grid(row=10, column=4)

state_housing_sb = Spinbox(help_label, text="State Housing", from_=0, to=5)
state_housing_sb.grid(row=10, column=5)

# state_pensions
def state_pensions_pop():
   messagebox.showinfo("State Pensions", "Rather than leave it up to the individual to provide for themselves after retirement, state pensions can guarantee a minimum standard of living for the elderly. Be aware that as life expectancy rises, the cost to the state of paying out pensions increases hugely. The level of state pension may encourage or discourage citizens to save into private pension plans.")
state_pensions = Button(help_label, text= "State Pensions",font=Body, command = state_pensions_pop)
state_pensions.grid(row=11, column=4)

state_pensions_sb = Spinbox(help_label, text="State Pensions", from_=0, to=5)
state_pensions_sb.grid(row=11, column=5)

# state_schools
def state_schools_pop():
   messagebox.showinfo("State Schools", "Free education for all ensures high levels of literacy and can be beneficial to the economy, especially those parts of the economy requiring a skilled workforce. The flipside of this is that state education can be expensive for the government. Wealthy individuals, not making use of state schools, may resent subsidizing them.")
state_schools = Button(help_label, text= "State Schools",font=Body, command = state_schools_pop)
state_schools.grid(row=12, column=4)

state_schools_sb = Spinbox(help_label, text="State Schools", from_=0, to=5)
state_schools_sb.grid(row=12, column=5)

# stem_cells
def stem_cells_pop():
   messagebox.showinfo("Stem Cells", "A stem cell is a primitive type of cell that can be developed into most of the types of cells found in the human body. Some scientists claim that stem cell research offers great hope for curing diseases such as diabetes and multiple sclerosis. However, because stem cells are taken from discarded human embryos, many 'pro-life' and religious groups oppose their usage.")
stem_cells = Button(help_label, text= "Stem Cells",font=Body, command = stem_cells_pop)
stem_cells.grid(row=13, column=4)

stem_cells_sb = Spinbox(help_label, text="Stem Cells", from_=0, to=5)
stem_cells_sb.grid(row=13, column=5)

# tax_shelters
def tax_shelters_pop():
   messagebox.showinfo("Tax Shelters", "By not fully taxing the wealth of the super-rich, tax shelters can be a great way to encourage successful entrepreneurs to make our country their home. With an ever-shrinking world, the rich are free to settle wherever they please. encouraging them to live here may mean that they spend their wealth in this country. Such measures can be very unpopular with the poor, who resent paying tax on their much lower earnings.")
tax_shelters = Button(help_label, text= "Tax Shelters",font=Body, command = tax_shelters_pop)
tax_shelters.grid(row=14, column=4)

tax_shelters_sb = Spinbox(help_label, text="Tax Shelters", from_=0, to=5)
tax_shelters_sb.grid(row=14, column=5)

# technology_colleges
def technology_colleges_pop():
   messagebox.showinfo("Technology Colleges", "Technology colleges are 'specialist schools' with a focus on computer literacy, biotechnology and similar subjects. These state-run colleges receive special funding from central government in order to encourage a greater level of technological literacy amongst the future workforce.")
technology_colleges = Button(help_label, text= "Technology Colleges",font=Body, command = technology_colleges_pop)
technology_colleges.grid(row=15, column=4)

technology_colleges_sb = Spinbox(help_label, text="Technology Colleges", from_=0, to=5)
technology_colleges_sb.grid(row=15, column=5)

# technology_grants
def technology_grants_pop():
   messagebox.showinfo("Technology Grants", "The government can provide state funding to encourage business to invest in new and exciting technologies. Although this helps give us a competitive advantage and can create jobs, it can be argued that its an unnecessary distortion of the market.")
technology_grants = Button(help_label, text= "Technology Grants",font=Body, command = technology_grants_pop)
technology_grants.grid(row=16, column=4)

technology_grants_sb = Spinbox(help_label, text="Technology Grants", from_=0, to=5)
technology_grants_sb.grid(row=16, column=5)

# telecommuting_initiative
def telecommuting_initiative_pop():
   messagebox.showinfo("Telecommuting Initiative", "Telecommuting, or 'working from home' is seen as desirable because it reduces the pressure on the transport infrastructure, and can be an improvement to people's quality of life. It's also welcomed by parents. This policy offers tax incentives to companies supporting this option.")
telecommuting_initiative = Button(help_label, text= "Telecommuting Initiative",font=Body, command = telecommuting_initiative_pop)
telecommuting_initiative.grid(row=17, column=4)

telecommuting_initiative_sb = Spinbox(help_label, text="Telecommuting Initiative", from_=0, to=5)
telecommuting_initiative_sb.grid(row=17, column=5)

# tobacco_tax
def tobacco_tax_pop():
   messagebox.showinfo("Tobacco Tax", "Despite the failure of tobacco companies to admit it, there is good reason to believe that smoking has negative effects on health. This is used as a justification for taxing tobacco. Cynics point out that the government benefits hugely from a tax on a product it is supposedly against. Health campaigners encourage the tax as a way to encourage a more healthy population")
tobacco_tax = Button(help_label, text= "Tobacco Tax",font=Body, command = tobacco_tax_pop)
tobacco_tax.grid(row=18, column=4)

tobacco_tax_sb = Spinbox(help_label, text="Tobacco Tax", from_=0, to=5)
tobacco_tax_sb.grid(row=18, column=5)

# toll_roads
def toll_roads_pop():
   messagebox.showinfo("Toll Roads", "Toll roads charge motorists to use specific roads (normally major highways). This is a great example of directly applying market forces, by only charging those who use a particular route for the construction and maintenance of that route. Motorists tend to see this as just another form of taxation, whereas commuters appreciate not being charged for roads they seldom use.")
toll_roads = Button(help_label, text= "Toll Roads",font=Body, command = toll_roads_pop)
toll_roads.grid(row=19, column=4)

toll_roads_sb = Spinbox(help_label, text="Toll Roads", from_=0, to=5)
toll_roads_sb.grid(row=19, column=5)

# unemployed_benefit
def unemployed_benefit_pop():
   messagebox.showinfo("Unemployed Benefit", "Unemployment benefit is a state benefit given to everyone who is able to work but cannot find employment. Socialists regard this as a minimum safety net for workers out of work because of the whims of the economy. Some believe that high unemployment benefits distort the market and discourage people from seeking work.")
unemployed_benefit = Button(help_label, text= "Unemployed Benefit",font=Body, command = unemployed_benefit_pop)
unemployed_benefit.grid(row=20, column=4)

unemployed_benefit_sb = Spinbox(help_label, text="Unemployed Benefit", from_=0, to=5)
unemployed_benefit_sb.grid(row=20, column=5)

# university_grants
def university_grants_pop():
   messagebox.showinfo("University Grants", "Although not all citizens will pursue a university education, governments can provide subsidies to students to encourage a more educated workforce. University grants also ensure equality of opportunity, as in their absence the cost of a university education can be beyond the reach of working class families.")
university_grants = Button(help_label, text= "University Grants",font=Body, command = university_grants_pop)
university_grants.grid(row=21, column=4)

university_grants_sb = Spinbox(help_label, text="University Grants", from_=0, to=5)
university_grants_sb.grid(row=21, column=5)

# welfare_fraud_dept
def welfare_fraud_dept_pop():
   messagebox.showinfo("Welfare Fraud Dept", "When government gives so much money out in welfare payments, it's essential that the money is correctly targeted and not exploited by people making spurious claims. A dedicated fraud department will detect false claimants, recover lost money and reassure middle income tax payers that their taxes are being spent wisely, although it can antagonize legitimate claimants.")
welfare_fraud_dept = Button(help_label, text= "Welfare Fraud Dept",font=Body, command = welfare_fraud_dept_pop)
welfare_fraud_dept.grid(row=22, column=4)

welfare_fraud_dept_sb = Spinbox(help_label, text="Welfare Fraud Dept", from_=0, to=5)
welfare_fraud_dept_sb.grid(row=22, column=5)

# winter_fuel_subsidy
def winter_fuel_subsidy_pop():
   messagebox.showinfo("Winter Fuel Subsidy", "A special concession given to the elderly. This is a regular welfare payment made to everyone over retirement age towards the cost of their winter fuel bills. It is designed to reduce 'fuel poverty' which can occur when some elderly members of society cannot afford to heat their homes in winter.")
winter_fuel_subsidy = Button(help_label, text= "Winter Fuel Subsidy",font=Body, command = winter_fuel_subsidy_pop)
winter_fuel_subsidy.grid(row=23, column=4)

winter_fuel_subsidy_sb = Spinbox(help_label, text="Winter Fuel Subsidy", from_=0, to=5)
winter_fuel_subsidy_sb.grid(row=23, column=5)

# work_safety_law
def work_safety_law_pop():
   messagebox.showinfo("Work Safety Law", "Work safety law, often known as 'health and safety' is a series of measures to ensure employees are not at risk from injury in their day-to-day activities. Trade unionists often hail such laws as a valuable defense against unscrupulous employers who may put lives at risk. Many business leaders are concerned at the high levels of bureaucracy and restrictive practices that can result from such laws, which they see as a burden on business.")
work_safety_law = Button(help_label, text= "Work Safety Law",font=Body, command = work_safety_law_pop)
work_safety_law.grid(row=24, column=4)

work_safety_law_sb = Spinbox(help_label, text="Work Safety Law", from_=0, to=5)
work_safety_law_sb.grid(row=24, column=5)

# youth_club_subsidies
def youth_club_subsidies_pop():
   messagebox.showinfo("Youth Club Subsidies", "Free youth clubs ensure that teenagers have a 'place to go' which can help them to stay out of trouble, and in the long run, reduce the incidence of street crime. It can be resented by some wealthier taxpayers, who see it as an unnecessary expense, paid for by their taxes.")
youth_club_subsidies = Button(help_label, text= "Youth Club Subsidies",font=Body, command = youth_club_subsidies_pop)
youth_club_subsidies.grid(row=25, column=4)

youth_club_subsidies_sb = Spinbox(help_label, text="Youth Club Subsidies", from_=0, to=5)
youth_club_subsidies_sb.grid(row=25, column=5)

# abortion_law
def abortion_law_pop():
   messagebox.showinfo("Abortion Law", "Few areas of policy incite stronger emotions that the debate over abortion. On the 'pro-life' side, are arguments about the rights of the unborn child, and arguments are often made from a  religious standpoint. On the 'pro-choice' side, there is the argument that the State should not have more say over what a woman does with her body than she does. Making any change to the States position on abortion requires a hefty amount of political capital.")
abortion_law = Button(help_label, text= "Abortion Law",font=Body, command = abortion_law_pop)
abortion_law.grid(row=26, column=4)

abortion_law_sb = Spinbox(help_label, text="Abortion Law", from_=0, to=5)
abortion_law_sb.grid(row=26, column=5)

# rent_controls
def rent_controls_pop():
   messagebox.showinfo("Rent Controls", "An alternative to state-housing is a system where the state will regulate the private-rental market in a bid to ensure the supply of affordable housing for all, even within the private sector. Capitalists will naturally see this as a distortion of the free market that will prevent enough homes being built, whereas supporters will say it prevents exploitation of the poor by greedy landlords.")
rent_controls = Button(help_label, text= "Rent Controls",font=Body, command = rent_controls_pop)
rent_controls.grid(row=27, column=4)

rent_controls_sb = Spinbox(help_label, text="Rent Controls", from_=0, to=5)
rent_controls_sb.grid(row=27, column=5)

# school_vouchers
def school_vouchers_pop():
   messagebox.showinfo("School Vouchers", "A measure designed to encourage the growth of private schooling, whilst still enabling everyone to afford an education. School  vouchers are issued by the State to parents for each child which they can then spend in the private sector on education. This is a different approach to pure state schooling because with school tax credits the schools are privately run and the teachers are no longer state employees.")
school_vouchers = Button(help_label, text= "School Vouchers",font=Body, command = school_vouchers_pop)
school_vouchers.grid(row=28, column=4)

school_vouchers_sb = Spinbox(help_label, text="School Vouchers", from_=0, to=5)
school_vouchers_sb.grid(row=28, column=5)

# oil_drilling_subsidy
def oil_drilling_subsidy_pop():
   messagebox.showinfo("Oil Drilling Subsidy", "To encourage investment in new oil and gas drilling, and thus raise the supply of fossil fuel energy for the country, these tax breaks effectively subsidize fossil fuels. This will indirectly reduce fuel prices and stimulate the economy, but will be an outrage to environmentalists.")
oil_drilling_subsidy = Button(help_label, text= "Oil Drilling Subsidy",font=Body, command = oil_drilling_subsidy_pop)
oil_drilling_subsidy.grid(row=29, column=4)

oil_drilling_subsidy_sb = Spinbox(help_label, text="Oil Drilling Subsidy", from_=0, to=5)
oil_drilling_subsidy_sb.grid(row=29, column=5)

# mansion_tax
def mansion_tax_pop():
   messagebox.showinfo("Mansion Tax", "A special high rate of tax charged annually on the ownership of super-expensive homes. This tax is popular with some because it is almost impossible to avoid, as homes cannot be easily hidden. It is perceived as unfair by some elderly people who may have expensive homes but relatively low incomes, and thus have difficulty in paying the annual tax. It is a form of wealth-tax, as opposed to income tax.")
mansion_tax = Button(help_label, text= "Mansion Tax",font=Body, command = mansion_tax_pop)
mansion_tax.grid(row=30, column=4)

mansion_tax_sb = Spinbox(help_label, text="Mansion Tax", from_=0, to=5)
mansion_tax_sb.grid(row=30, column=5)

# fuel_efficiency
def fuel_efficiency_pop():
   messagebox.showinfo("Fuel Efficiency", "Mandatory standards for new cars which dictate the minimum level of fuel efficiency. This is a long term measure aimed to raise the fuel efficiency of the country's cars, and thus reduce our dependence on oil, as well as reducing the cost of driving over the long term. It will be unpopular with car manufacturers, but a hit with environmentalists.")
fuel_efficiency = Button(help_label, text= "Fuel Efficiency",font=Body, command = fuel_efficiency_pop)
fuel_efficiency.grid(row=31, column=4)

fuel_efficiency_sb = Spinbox(help_label, text="Fuel Efficiency", from_=0, to=5)
fuel_efficiency_sb.grid(row=31, column=5)

# foreign_investor_tax_breaks
def foreign_investor_tax_breaks_pop():
   messagebox.showinfo("Foreign Investor Tax Breaks", "Special tax breaks given to large foreign-owned multinational companies to encourage them to invest in our country. This could include tax-free periods, introductory rates of corporate tax, and straight subsidies to encourage investment. Helps to encourage investment from overseas, but will be seen as incredibly unpatriotic, and pandering to the whims of huge foreign capitalist organizations.")
foreign_investor_tax_breaks = Button(help_label, text= "Foreign Investor Tax Breaks",font=Body, command = foreign_investor_tax_breaks_pop)
foreign_investor_tax_breaks.grid(row=32, column=4)

foreign_investor_tax_breaks_sb = Spinbox(help_label, text="Foreign Investor Tax Breaks", from_=0, to=5)
foreign_investor_tax_breaks_sb.grid(row=32, column=5)

# robotics_research
def robotics_research_pop():
   messagebox.showinfo("Robotics Research", "A special grant to encourage research in robotics. Robotics is a very long term area of research which will eventually bring about vast boosts in productivity, but at the same time it will reduce the amount of low or semi-skilled jobs in the economy, and thus potentially lead to higher unemployment.")
robotics_research = Button(help_label, text= "Robotics Research",font=Body, command = robotics_research_pop)
robotics_research.grid(row=33, column=4)

robotics_research_sb = Spinbox(help_label, text="Robotics Research", from_=0, to=5)
robotics_research_sb.grid(row=33, column=5)

# private_prisons
def private_prisons_pop():
   messagebox.showinfo("Private Prisons", "Rather than directly control and manage a State prison service, this policy allows prisons to be privately owned and managed, and merely paid for by the state. Private prisons could result in lower cost and higher efficiency. These measures will be unpopular with trade unionists. Liberals will have ethical concerns about profiting from incarceration, but still be pleased if spending is high enough to promote rehabilitation.")
private_prisons = Button(help_label, text= "Private Prisons",font=Body, command = private_prisons_pop)
private_prisons.grid(row=34, column=4)

private_prisons_sb = Spinbox(help_label, text="Private Prisons", from_=0, to=5)
private_prisons_sb.grid(row=34, column=5)

# junk_food_tax
def junk_food_tax_pop():
   messagebox.showinfo("Junk Food Tax", "A punitive tax rate charged on unhealthy food such as takeaway hamburgers, fizzy drinks and high sugar or fat content pre-processed food. Levied with the aim of improving the health of the nation, but can be unpopular.")
junk_food_tax = Button(help_label, text= "Junk Food Tax",font=Body, command = junk_food_tax_pop)
junk_food_tax.grid(row=35, column=4)

junk_food_tax_sb = Spinbox(help_label, text="Junk Food Tax", from_=0, to=5)
junk_food_tax_sb.grid(row=35, column=5)

# health_food_subsidies
def health_food_subsidies_pop():
   messagebox.showinfo("Health Food Subsidies", "A tax incentive that makes healthy food, such as fruit and vegetables, cheaper than the higher fat or higher sugar foods. Seen as an incentive to eat well, rather than a punishment for eating badly, and thus less punitive on the poor than a 'fat tax'.")
health_food_subsidies = Button(help_label, text= "Health Food Subsidies",font=Body, command = health_food_subsidies_pop)
health_food_subsidies.grid(row=36, column=4)

health_food_subsidies_sb = Spinbox(help_label, text="Health Food Subsidies", from_=0, to=5)
health_food_subsidies_sb.grid(row=36, column=5)

# tasers
def tasers_pop():
   messagebox.showinfo("Tasers", "A non-lethal but still highly effective (and possibly dangerous) weapon which effectively gives criminals an electric shock. Supporters say it is a good compromise between the need to disable violent criminals and the risk of death associated with traditional firearms. Opponents claim that the use of such weapons lowers the barrier-to-use for the police and will encourage more casual use of force against the population.")
tasers = Button(help_label, text= "Tasers",font=Body, command = tasers_pop)
tasers.grid(row=0, column=6)

tasers_sb = Spinbox(help_label, text="Tasers", from_=0, to=5)
tasers_sb.grid(row=0, column=7)

# police_drones
def police_drones_pop():
   messagebox.showinfo("Police Drones", "Unmanned aerial reconnaissance vehicles, similar to remote control planes which can be employed by the police force. The 'eye in the sky' is a useful way to keep track of mobs and rioters, and allows for subtle yet effective surveillance. The police see it as a vital tool for modern crime fighting, but there are concerns that this is a step further towards a big-brother style surveillance society where everyone is tracked.")
police_drones = Button(help_label, text= "Police Drones",font=Body, command = police_drones_pop)
police_drones.grid(row=1, column=6)

police_drones_sb = Spinbox(help_label, text="Police Drones", from_=0, to=5)
police_drones_sb.grid(row=1, column=7)

# arts_subsidies
def arts_subsidies_pop():
   messagebox.showinfo("Arts Subsidies", "Investing public money in the arts is controversial with capitalists who see it as supporting uneconomic elitist entertainment, but others see it as vital to a countries culture, boosting our image on the world stage, and attracting tourists.")
arts_subsidies = Button(help_label, text= "Arts Subsidies",font=Body, command = arts_subsidies_pop)
arts_subsidies.grid(row=2, column=6)

arts_subsidies_sb = Spinbox(help_label, text="Arts Subsidies", from_=0, to=5)
arts_subsidies_sb.grid(row=2, column=7)

# healthcare_vouchers
def healthcare_vouchers_pop():
   messagebox.showinfo("Healthcare Vouchers", "A measure designed to encourage the growth of private health care whilst still enabling everyone access to it. Healthcare vouchers are  issued by the State to everyone but can then only be spent in the private sector on health care. This is a different approach to pure State health care because with health tax credits, the hospitals are privately run and the medical staff are no longer state employees.")
healthcare_vouchers = Button(help_label, text= "Healthcare Vouchers",font=Body, command = healthcare_vouchers_pop)
healthcare_vouchers.grid(row=3, column=6)

healthcare_vouchers_sb = Spinbox(help_label, text="Healthcare Vouchers", from_=0, to=5)
healthcare_vouchers_sb.grid(row=3, column=7)

# health_tax_credits
def health_tax_credits_pop():
   messagebox.showinfo("Health Tax Credits", "A system of tax-reductions and credits designed to encourage people to spend their money on private healthcare, in order to reduce their tax liability. This boosts healthcare without involving the state running hospitals or employing doctors, but it's effect is limited to those people in society earning enough to be paying tax in the first place.")
health_tax_credits = Button(help_label, text= "Health Tax Credits",font=Body, command = health_tax_credits_pop)
health_tax_credits.grid(row=4, column=6)

health_tax_credits_sb = Spinbox(help_label, text="Health Tax Credits", from_=0, to=5)
health_tax_credits_sb.grid(row=4, column=7)

# school_tax_credits
def school_tax_credits_pop():
   messagebox.showinfo("School Tax Credits", "A system of tax-reductions and credits designed to encourage people to spend their money on private education in order to reduce their tax liability. This boosts private schooling without involving the State running schools or employing teachers but it's effect is limited to those people in society earning enough to be paying tax in the first place.")
school_tax_credits = Button(help_label, text= "School Tax Credits",font=Body, command = school_tax_credits_pop)
school_tax_credits.grid(row=5, column=6)

school_tax_credits_sb = Spinbox(help_label, text="School Tax Credits", from_=0, to=5)
school_tax_credits_sb.grid(row=5, column=7)

# food_stamps
def food_stamps_pop():
   messagebox.showinfo("Food Stamps", "Food stamps is a system where the state will issue vouchers or 'stamps' to those citizens on low or no income, to ensure they are able to afford food. Unlike giving a straight cash benefit, food stamps can only be redeemed for uncooked food, preventing them being used for unhealthy takeaway food. Supporters see food stamps as a valuable way to ensure nobody goes hungry, no matter their income. Critics consider such a scheme patronizing, and no more than papering over the cracks caused by free market failure and low wages.")
food_stamps = Button(help_label, text= "Food Stamps",font=Body, command = food_stamps_pop)
food_stamps.grid(row=6, column=6)

food_stamps_sb = Spinbox(help_label, text="Food Stamps", from_=0, to=5)
food_stamps_sb.grid(row=6, column=7)

# food_standards
def food_standards_pop():
   messagebox.showinfo("Food Standards", "A food standards agency is a branch of government dedicated to ensuring the safety and minimum nutritional standards of food supplied within the country. Farmers may regard the agency as an extra layer of bureaucracy and meddling, but public health campaigners see the agency as an essential line of defense between the consumer and unscrupulous food producers looking to cut costs.")
food_standards = Button(help_label, text= "Food Standards",font=Body, command = food_standards_pop)
food_standards.grid(row=7, column=6)

food_standards_sb = Spinbox(help_label, text="Food Standards", from_=0, to=5)
food_standards_sb.grid(row=7, column=7)

# enterprise_investment_scheme
def enterprise_investment_scheme_pop():
   messagebox.showinfo("Enterprise Investment Scheme", "The Enterprise Investment Scheme is a system which gives tax breaks to wealthy individuals who invest their money in small startup companies which are based in this country. The scheme encourages investment in companies which should eventually grow and stimulate the economy, whilst at the same time giving a popular tax break to people who invest in them. Obviously indirectly, the scheme is being subsidized by those without savings to invest.")
enterprise_investment_scheme = Button(help_label, text= "Enterprise Investment Scheme",font=Body, command = enterprise_investment_scheme_pop)
enterprise_investment_scheme.grid(row=8, column=6)

enterprise_investment_scheme_sb = Spinbox(help_label, text="Enterprise Investment Scheme", from_=0, to=5)
enterprise_investment_scheme_sb.grid(row=8, column=7)

# recreational_drugs_tax
def recreational_drugs_tax_pop():
   messagebox.showinfo("Recreational Drugs Tax", "In societies that have legalized drugs such as Cannabis and Marijuana, there is a temptation to treat consumption of these drugs as a source of government revenue, given the claims that their consumption should be politely discouraged due to the negative effects on citizens health, in a similar way to governments taxing alcohol or tobacco.")
recreational_drugs_tax = Button(help_label, text= "Recreational Drugs Tax",font=Body, command = recreational_drugs_tax_pop)
recreational_drugs_tax.grid(row=9, column=6)

recreational_drugs_tax_sb = Spinbox(help_label, text="Recreational Drugs Tax", from_=0, to=5)
recreational_drugs_tax_sb.grid(row=9, column=7)

# Export button
export_button = Button(root, text="Export Info", font=Title)
export_button.grid(row= 0, column=2, ipady= 50, ipadx= 70)
root.mainloop()