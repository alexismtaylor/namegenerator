####Animal Adjective Name Generator
from __future__ import print_function
import random, string

def userLoop():
	letter = None
	while not letter or letter not in string.letters:
	    letter = str(raw_input("What letter would you like to use? (Cannot be X)\n"))
	    if letter == 'x' or letter == 'X':
	    	letter = None
	    else:
	    	choice = letter.upper()
	adjList = adjDict[choice]
	anList = animalDict[choice]

	adjective = random.choice(adjList)
	animal = random.choice(anList)

	if "-" in adjective:
		if "-" in animal:
			print("Try this: " + adjective.replace("-", " ").title() + " " + animal.replace("-", " ").title())
		else:
			print("Try this: " + adjective.replace("-", " ").title() + " " + animal.title())
	else:
		if "-" in animal:
			print("Try this: " + adjective.title() + " " + animal.replace("-", " ").title())
		else:
			print("Try this: " + adjective.title() + " " + animal.title())


aStr = "aback abaft abandoned abashed aberrant abhorrent abiding abject ablaze able abnormal aboard aboriginal abortive abounding abrasive abrupt absent absolute absorbed absorbing abstracted absurd abundant abusive academic acceptable accessible accidental acclaimed accomplished accurate aching acid acidic acoustic acrid acrobatic active actual actually ad hoc adamant adaptable addicted adept adhesive adjoining admirable admired adolescent adorable adored advanced adventurous affectionate afraid aged aggravating aggressive agile agitated agonizing agreeable ahead ajar alarmed alarming alcoholic alert alienated alike alive all alleged alluring aloof altruistic amazing ambiguous ambitious amiable ample amuck amused amusing anchored ancient ancient angelic angry angry anguished animated annoyed annoying annual another antique antsy anxious any apathetic appetizing apprehensive appropriate apt aquatic arctic arid aromatic arrogant artistic ashamed aspiring assorted assured astonishing athletic attached attentive attractive auspicious austere authentic authorized automatic available avaricious average awake aware awesome awful awkward axiomatic"
bStr = "babyish back bad baggy barbarous bare barren bashful basic batty bawdy beautiful beefy befitting belated belligerent beloved beneficial bent berserk best better bewildered bewitched big big-hearted billowy biodegradable bite-sized biting bitter bizarre black black-and-white bland blank blaring bleak blind blissful blond bloody blue blue-eyed blushing bogus boiling bold bony boorish bored boring bossy both bouncy boundless bountiful bowed brainy brash brave brawny breakable breezy brief bright brilliant brisk broad broken bronze brown bruised bubbly bulky bumpy buoyant burdensome burly bustling busy buttery buzzing"
cStr = "cagey calculating callous calm candid canine capable capital capricious carefree careful careless caring cautious cavernous ceaseless celebrated certain changeable charming cheap cheeky cheerful cheery chemical chief childlike chilly chivalrous chubby chunky circular clammy classic classy clean clear clear-cut clever cloistered close closed cloudy clueless clumsy cluttered coarse coherent cold colorful colorless colossal colossal combative comfortable common compassionate competent complete complex complicated composed concerned concrete condemned condescending confused conscious considerate constant contemplative content conventional convincing convoluted cooing cooked cool cooperative coordinated corny corrupt costly courageous courteous cowardly crabby crafty craven crazy creamy creative creepy criminal crisp critical crooked crowded cruel crushing cuddly cultivated cultured cumbersome curious curly curved curvy cut cute cylindrical cynical"
dStr = "daffy daily damaged damaging damp dangerous dapper dapper daring dark darling dashing dazzling dead deadly deadpan deafening dear dearest debonair decayed deceitful decent decimal decisive decorous deep deeply defeated defective defenseless defensive defiant deficient definite delayed delectable delicate delicious delightful delirious demanding demonic dense dental dependable dependent depraved depressed deranged descriptive deserted despicable detailed determined devilish devoted didactic different difficult digital dilapidated diligent dim diminutive dimpled dimwitted direct direful dirty disagreeable disastrous discreet discrete disfigured disguised disgusted disgusting dishonest disillusioned disloyal dismal dispensable distant distinct distorted distraught distressed disturbed divergent dizzy domineering dopey doting double doubtful downright drab draconian drafty drained dramatic dreary droopy drunk dry dual dull dull dusty dutiful dynamic dysfunctional"
eStr = "each eager early earnest earsplitting earthy easy easy-going eatable economic ecstatic edible educated efficacious efficient eight elaborate elastic elated elderly electric elegant elementary elfin elite elliptical emaciated embarrassed embellished eminent emotional empty enchanted enchanting encouraging endurable energetic enlightened enormous enraged entertaining enthusiastic entire envious envious equable equal equatorial erect erratic essential esteemed ethereal ethical euphoric evanescent evasive even evergreen everlasting every evil exalted exasperated excellent excitable excited exciting exclusive exemplary exhausted exhilarated exotic expensive experienced expert extensive extra-large extraneous extra-small extroverted exuberant exultant"
fStr = "fabulous faded failing faint fair faithful fake fallacious false familiar famous fanatical fancy fantastic far faraway far-flung far-off fascinated fast fat fatal fatherly faulty favorable favorite fearful fearless feeble feigned feisty feline female feminine fertile festive few fickle fierce filthy fine finicky finished firm first firsthand fitting five fixed flagrant flaky flamboyant flashy flat flawed flawless flickering flimsy flippant floppy flowery flufy fluid flustered fluttering foamy focused fond foolhardy foolish forceful foregoing forgetful forked formal forsaken forthright fortunate four fragile fragrant frail frank frantic frayed free freezing French frequent fresh fretful friendly frightened frightening frigid frilly frivolous frizzy front frosty frothy frozen frugal fruitful frustrating full fumbling fumbling functional funny furry furtive fussy future futuristic fuzzy"
gStr = "gabby gainful gamy gaping gargantuan garrulous gaseous gaudy general general generous gentle genuine ghastly giant giddy gifted gigantic giving glamorous glaring glass gleaming gleeful glib glistening glittering gloomy glorious glossy glum godly golden good good-natured goofy gorgeous graceful gracious grand grandiose grandiose granular grateful gratis grave gray greasy great greedy green gregarious grey grieving grim grimy gripping grizzled groovy gross grotesque grouchy grounded growing growling grown grubby gruesome grumpy guarded guiltless guilty gullible gummy gusty guttural"
hStr = "habitual hairy half half hallowed halting handmade handsome handsomely handy hanging hapless happy happy-go-lucky hard hard-to-find harebrained harmful harmless harmonious harsh hasty hateful haunting heady healthy heartbreaking heartfelt hearty heavenly heavy hefty hellish helpful helpless hesitant hidden hideous high highfalutin high-level high-pitched hilarious hissing historical hoarse holistic hollow homeless homely honest honorable honored hopeful horrible horrific hospitable hot huge hulking humble humdrum humiliating humming humongous humorous hungry hurried hurt hurtful hushed husky hypnotic hysterical"
iStr = "icky icy ideal ideal idealistic identical idiotic idle idolized ignorant ill illegal ill-fated ill-informed illiterate illustrious imaginary imaginative immaculate immaterial immediate immense imminent impartial impassioned impeccable imperfect imperturbable impish impolite important imported impossible impractical impressionable impressive improbable impure inborn incandescent incomparable incompatible incompetent incomplete inconclusive inconsequential incredible indelible indolent industrious inexpensive inexperienced infamous infantile infatuated inferior infinite informal innate innocent inquisitive insecure insidious insignificant insistent instinctive instructive insubstantial intelligent intent intentional interesting internal international intrepid intrigued invincible irate ironclad irresponsible irritable irritating itchy"
jStr = "jaded jagged jam-packed jaunty jazzy jealous jittery jobless joint jolly jovial joyful joyous jubilant judicious juicy jumbled jumbo jumpy jumpy junior juvenile"
kStr = "kaleidoscopic kaput keen key kind kindhearted kindly klutzy knobby knotty knowing knowledgeable known kooky kosher"
lStr = "labored lackadaisical lacking lame lame lamentable languid lanky large last lasting late laughable lavish lawful lazy leading leafy lean learned left legal legitimate lethal level lewd light lighthearted likable like likeable likely limited limp limping linear lined liquid literate little live lively livid living loathsome lone lonely long longing long-term loose lopsided lost loud loutish lovable lovely loving low lowly loyal lucky ludicrous lumbering luminous lumpy lush lustrous luxuriant luxurious lying lyrical"
mStr = "macabre macho mad maddening made-up madly magenta magical magnificent majestic major makeshift male malicious mammoth maniacal many marked married marvelous masculine massive material materialistic mature meager mealy mean measly meaty medical mediocre medium meek melancholy mellow melodic melted memorable menacing merciful mere merry messy metallic mighty mild military milky mindless miniature minor minty minute miscreant miserable miserly misguided mistaken misty mixed moaning modern modest moist moldy momentous monstrous monthly monumental moody moral mortified motherly motionless mountainous muddled muddy muffled multicolored mundane mundane murky mushy musty mute muted mysterious"
nStr = "naive nappy narrow nasty natural naughty nauseating nautical near neat nebulous necessary needless needy negative neglected negligible neighboring neighborly nervous nervous new next nice nice nifty nimble nine nippy nocturnal noiseless noisy nonchalant nondescript nonsensical nonstop normal nostalgic nosy notable noted noteworthy novel noxious null numb numberless numerous nutritious nutty"
oStr = "oafish obedient obeisant obese oblivious oblong obnoxious obscene obsequious observant obsolete obtainable obvious occasional oceanic odd oddball offbeat offensive official oily old old-fashioned omniscient one onerous only open opposite optimal optimistic opulent orange orderly ordinary organic original ornate ornery ossified other our outgoing outlandish outlying outrageous outstanding oval overconfident overcooked overdue overjoyed overlooked overrated overt overwrought"
pStr = "painful painstaking palatable pale paltry panicky panoramic parallel parched parsimonious partial passionate past pastel pastoral pathetic peaceful penitent peppery perfect perfumed periodic perky permissible perpetual perplexed personal pertinent pesky pessimistic petite petty petty phobic phony physical picayune piercing pink piquant pitiful placid plain plaintive plant plastic plausible playful pleasant pleased pleasing plucky plump plush pointed pointless poised polished polite political pompous poor popular portly posh positive possessive possible potable powerful powerless practical precious premium present present prestigious pretty previous pricey prickly primary prime pristine private prize probable productive profitable profuse proper protective proud prudent psychedelic psychotic public puffy pumped punctual pungent puny pure purple purring pushy pushy putrid puzzled puzzling"
qStr = "quack quaint quaint qualified quarrelsome quarterly queasy querulous questionable quick quickest quick-witted quiet quintessential quirky quixotic quixotic quizzical"
rStr = "rabid racial radiant ragged rainy rambunctious rampant rapid rare rash raspy ratty raw ready real realistic reasonable rebel recent receptive reckless recondite rectangular red redundant reflecting reflective regal regular reliable relieved remarkable reminiscent remorseful remote repentant repulsive required resolute resonant respectful responsible responsive revolving rewarding rhetorical rich right righteous rightful rigid ringed ripe ritzy roasted robust romantic roomy rosy rotating rotten rotund rough round rowdy royal rubbery ruddy rude rundown runny rural rustic rusty ruthless"
sStr = "sable sad safe salty same sandy sane sarcastic sardonic sassy satisfied satisfying savory scaly scandalous scant scarce scared scary scattered scented scholarly scientific scintillating scornful scratchy scrawny screeching second secondary second-hand secret secretive sedate seemly selective self-assured selfish self-reliant sentimental separate serene serious serpentine several severe shabby shadowy shady shaggy shaky shallow shameful shameless sharp shimmering shiny shivering shocked shocking shoddy short short-term showy shrill shut shy sick silent silky silly silver similar simple simplistic sincere sinful single six sizzling skeletal skillful skinny sleepy slight slim slimy slippery sloppy slow slushy small smarmy smart smelly smiling smoggy smooth smug snappy snarling sneaky sniveling snobbish snoopy snotty sociable soft soggy solid somber some sophisticated sordid sore sorrowful soulful soupy sour sour Spanish sparkling sparse special specific spectacular speedy spherical spicy spiffy spiky spirited spiritual spiteful splendid spooky spotless spotted spotty spry spurious squalid square squeaky squealing squeamish squiggly stable staid stained staking stale standard standing starchy stark starry statuesque steadfast steady steel steep stereotyped sticky stiff stimulating stingy stormy stout straight strange strict strident striking striped strong studious stunning stunning stupendous stupid sturdy stylish subdued submissive subsequent substantial subtle suburban successful succinct succulent sudden sugary sulky sunny super superb superficial superior supportive supreme sure-footed surprised suspicious svelte swanky sweaty sweet sweltering swift sympathetic symptomatic synonymous"
tStr = "taboo tacit tacky talented talkative tall tame tan tangible tangy tart tasteful tasteless tasty tattered taut tawdry tearful tedious teeming teeny teeny-tiny telling temporary tempting ten tender tense tenuous tepid terrible terrific tested testy thankful that therapeutic these thick thin thinkable third thirsty thorny thorough those thoughtful thoughtless threadbare threatening three thrifty thundering thunderous tidy tight tightfisted timely tinted tiny tired tiresome toothsome torn torpid total tough towering tragic trained tranquil trashy traumatic treasured tremendous triangular tricky trifling trim trite trivial troubled truculent true trusting trustworthy trusty truthful tubby turbulent twin two typical"
uStr = "ubiquitous ugliest ugly ultimate ultra unable unaccountable unarmed unaware unbecoming unbiased uncomfortable uncommon unconscious uncovered understated understood undesirable unequal unequaled uneven unfinished unfit unfolded unfortunate unhappy unhealthy uniform unimportant uninterested unique united unkempt unknown unlawful unlined unlucky unnatural unpleasant unrealistic unripe unruly unselfish unsightly unsteady unsuitable unsung untidy untimely untried untrue unused unusual unwelcome unwieldy unwitting unwritten upbeat uppity upright upset uptight urban usable used used useful useless utilized utopian utter uttermost"
vStr = "vacant vacuous vagabond vague vain valid valuable vapid variable various vast velvety venerated vengeful venomous verdant verifiable versed vexed vibrant vicious victorious vigilant vigorous villainous violent violet virtual virtuous visible vital vivacious vivid voiceless volatile voluminous voracious vulgar"
wStr = "wacky waggish waiting wakeful wan wandering wanting warlike warm warmhearted warped wary wasteful watchful waterlogged watery wavy weak wealthy weary webbed wee weekly weepy weighty weird welcome well-documented well-groomed well-informed well-lit well-made well-off well-to-do well-worn wet which whimsical whirlwind whispered whispering white whole wholesale whopping wicked wide wide-eyed wiggly wild willing wilted winding windy winged wiry wise wistful witty wobbly woebegone woeful womanly wonderful wooden woozy wordy workable worldly worn worried worrisome worse worst worthless worthwhile worthy wrathful wretched writhing wrong wry"
yStr = "yawning yearly yellow yellowish yielding young youthful yummy"
zStr = "zany zealous zesty zigzag zippy zonked"

animalDict = {}
adjDict = {}

aAn = "Aardvark Abyssinian Adelie-Penguin Affenpinscher Afghan-Hound African-Bush-Elephant African-Civet African-Clawed-Frog African-Forest-Elephant African-Palm-Civet African-Penguin African-Tree-Toad African-Wild-Dog Ainu-Dog Airedale-Terrier Akbash Akita Alaskan-Malamute Albatross Aldabra-Giant-Tortoise Alligator Alpine-Dachsbracke American-Bulldog American-Cocker-Spaniel American-Coonhound American-Eskimo-Dog American-Foxhound American-Pit-Bull-Terrier American-Staffordshire-Terrier American-Water-Spaniel Anatolian-Shepherd-Dog Angelfish Ant Anteater Antelope Appenzeller-Dog Arctic-Fox Arctic-Hare Arctic-Wolf Armadillo Asian-Elephant Asian-Giant-Hornet Asian-Palm-Civet Asiatic-Black-Bear Australian-Cattle-Dog Australian-Kelpie-Dog Australian-Mist Australian-Shepherd Australian-Terrier Avocet Axolotl Aye-Aye"
bAn = "Baboon Bactrian-Camel Badger Balinese Banded-Palm-Civet Bandicoot Barb Barn-Owl Barnacle Barracuda Basenji-Dog Basking-Shark Basset-Hound Bat Bavarian-Mountain-Hound Beagle Bear Bearded-Collie Bearded-Dragon Beaver Bedlington-Terrier Beetle Bengal-Tiger Bernese-Mountain-Dog Bichon-Frise Binturong Bird Birds-Of-Paradise Birman Bison Black-Bear Black-Rhinoceros Black-Russian-Terrier Black-Widow-Spider Bloodhound Blue-Lacy-Dog Blue-Whale Bluetick-Coonhound Bobcat Bolognese-Dog Bombay Bongo Bonobo Booby Border-Collie Border-Terrier Bornean-Orang-utan Borneo-Elephant Boston-Terrier Bottle-Nosed-Dolphin Boxer-Dog Boykin-Spaniel Brazilian-Terrier Brown-Bear Budgerigar Buffalo Bull-Mastiff Bull-Shark Bull-Terrier Bulldog Bullfrog Bumble-Bee Burmese Burrowing-Frog Butterfly Butterfly-Fish"
cAn = "Caiman Caiman-Lizard Cairn-Terrier Camel Canaan-Dog Capybara Caracal Carolina-Dog Cassowary Cat Caterpillar Catfish Cavalier-King-Charles-Spaniel Centipede Cesky-Fousek Chameleon Chamois Cheetah Chesapeake-Bay-Retriever Chicken Chihuahua Chimpanzee Chinchilla Chinese-Crested-Dog Chinook Chinstrap-Penguin Chipmunk Chow-Chow Cichlid Clouded-Leopard Clown-Fish Clumber-Spaniel Coati Cockroach Collared-Peccary Collie Common-Buzzard Common-Frog Common-Loon Common-Toad Coral Cottontop-Tamarin Cougar Cow Coyote Crab Crab-Eating-Macaque Crane Crested-Penguin Crocodile Cross-River-Gorilla Curly-Coated-Retriever Cuscus Cuttlefish"
dAn = "Dachshund Dalmatian Darwin's-Frog Deer Desert-Tortoise Deutsche-Bracke Dhole Dingo Discus Doberman-Pinscher Dodo Dog Dogo-Argentino Dogue-De-Bordeaux Dolphin Donkey Dormouse Dragonfly Drever Duck Dugong Dunker Dusky-Dolphin Dwarf-Crocodile"
eAn = "Eagle Earwig Eastern-Gorilla Eastern-Lowland-Gorilla Echidna Edible-Frog Egyptian-Mau Electric-Eel Elephant Elephant-Seal Elephant-Shrew Emperor-Penguin Emperor-Tamarin Emu English-Cocker-Spaniel English-Shepherd English-Springer-Spaniel Entlebucher-Mountain-Dog Epagneul-Pont-Audemer Eskimo-Dog Estrela-Mountain-Dog"
fAn = "Falcon Fennec-Fox Ferret Field-Spaniel Fin-Whale Finnish-Spitz Fire-Bellied-Toad Fish Fishing-Cat Flamingo Flat-Coat-Retriever Flounder Fly Flying-Squirrel Fossa Fox Fox-Terrier French-Bulldog Frigatebird Frilled-Lizard Frog Fur-Seal"
gAn = "Galapagos-Penguin Galapagos-Tortoise Gar Gecko Gentoo-Penguin Geoffroys-Tamarin Gerbil German-Pinscher German-Shepherd Gharial Giant-African-Land-Snail Giant-Clam Giant-Panda-Bear Giant-Schnauzer Gibbon Gila-Monster Giraffe Glass-Lizard Glow-Worm Goat Golden-Lion-Tamarin Golden-Oriole Golden-Retriever Goose Gopher Gorilla Grasshopper Great-Dane Great-White-Shark Greater-Swiss-Mountain-Dog Green-Bee-Eater Greenland-Dog Grey-Mouse-Lemur Grey-Reef-Shark Grey-Seal Greyhound Grizzly-Bear Grouse Guinea-Fowl Guinea-Pig Guppy"
hAn = "Hammerhead-Shark Hamster Hare Harrier Havanese Hedgehog Hercules-Beetle Hermit-Crab Heron Highland-Cattle Himalayan Hippopotamus Honey-Bee Horn-Shark Horned-Frog Horse Horseshoe-Crab Howler-Monkey Human Humboldt-Penguin Hummingbird Humpback-Whale Hyena"
iAn = "Ibis Ibizan-Hound Iguana Impala Indian-Elephant Indian-Palm-Squirrel Indian-Rhinoceros Indian-Star-Tortoise Indochinese-Tiger Indri Insect Irish-Setter Irish-WolfHound"
jAn = "Jack-Russel Jackal Jaguar Japanese-Chin Japanese-Macaque Javan-Rhinoceros Javanese Jellyfish"
kAn = "Kakapo Kangaroo Keel-Billed-Toucan Killer-Whale King-Crab King-Penguin Kingfisher Kiwi Koala Komodo-Dragon Kudu"
lAn = "Labradoodle Labrador-Retriever Ladybird Leaf-Tailed-Gecko Lemming Lemur Leopard Leopard-Cat Leopard-Seal Leopard-Tortoise Liger Lion Lionfish Little-Penguin Lizard Llama Lobster Long-Eared-Owl Lynx"
mAn = "Macaroni-Penguin Macaw Magellanic-Penguin Magpie Maine-Coon Malayan-Civet Malayan-Tiger Maltese Manatee Mandrill Manta-Ray Marine-Toad Markhor Marsh-Frog Masked-Palm-Civet Mastiff Mayfly Meerkat Millipede Minke-Whale Mole Molly Mongoose Mongrel Monitor-Lizard Monkey Monte-Iberia-Eleuth Moorhen Moose Moray-Eel Moth Mountain-Gorilla Mountain-Lion Mouse Mule"
nAn = "Neanderthal Neapolitan-Mastiff Newfoundland-Newt Nightingale Norfolk-Terrier Norwegian-Forest Numbat Nurse-Shark"
oAn = "Ocelot Octopus Okapi Old-English-Sheepdog Olm Opossum Orangutan Ostrich Otter Oyster"
pAn = "Pademelon Panther Parrot Patas-Monkey Peacock Pekingese Pelican Penguin Persian Pheasant Pied-Tamarin Pig Pika Pike Pink-Fairy-Armadillo Piranha Platypus Pointer Poison-Dart-Frog Polar-Bear Pond-Skater Poodle Pool-Frog Porcupine Possum Prawn Proboscis-Monkey Puffer-Fish Puffin Pug Puma Purple-Emperor Puss-Moth Pygmy-Hippopotamus Pygmy-Marmoset"
qAn = "Quail Quetzal Quokka Quoll"
rAn = "Rabbit Raccoon Raccoon-Dog Radiated-Tortoise Ragdoll Rat Rattlesnake Red-Knee-Tarantula Red-Panda Red-Wolf Red-handed-Tamarin Reindeer Rhinoceros River-Dolphin River-Turtle Robin Rock-Hyrax Rockhopper-Penguin Roseate-Spoonbill Rottweiler Royal-Penguin Russian-Blue"
sAn = "Sabre-Toothed-Tiger Saint-Bernard Salamander Sand-Lizard Saola Scorpion Scorpion-Fish Sea-Dragon Sea-Lion Sea-Otter Sea-Slug Sea-Squirt Sea-Turtle Sea-Urchin Seahorse Seal Serval Sheep Shih-Tzu Shrimp Siamese Siamese-Fighting-Fish Siberian Siberian-Husky Siberian-Tiger Silver-Dollar Skunk Sloth Slow-Worm Snail Snake Snapping-Turtle Snowshoe Snowy-Owl Somali South-China-Tiger Spadefoot-Toad Sparrow Spectacled-Bear Sperm-Whale Spider-Monkey Spiny-Dogfish Sponge Squid Squirrel Squirrel-Monkey Sri-Lankan-Elephant Staffordshire-Bull-Terrier Stag-Beetle Starfish Stellers-Sea-Cow Stick-Insect Stingray Stoat Striped-Rocket-Frog Sumatran-Elephant Sumatran-Orang-utan Sumatran-Rhinoceros Sumatran-Tiger Sun-Bear Swan"
tAn = "Tang Tapir Tarsier Tasmanian-Devil Tawny-Owl Termite Tetra Thorny-Devil Tibetan-Mastiff Tiffany Tiger Tiger-Salamander Tiger-Shark Tortoise Toucan Tree-Frog Tropicbird Tuatara Turkey Turkish-Angora"
uAn = "Uakari Uguisi Umbrellabird"
vAn = "Vampire-Bat Vervet-Monkey Vulture"
wAn = "Wallaby Walrus Warthog Wasp Water-Buffalo Water-Dragon Water-Vole Weasel Welsh-Corgi West-Highland-Terrier Western-Gorilla Western-Lowland-Gorilla Whale-Shark Whippet White-Faced-Capuchin White-Rhinoceros White-Tiger Wild-Boar Wildebeest Wolf Wolverine Wombat Woodlouse Woodpecker Woolly-Mammoth Woolly-Monkey Wrasse"
yAn = "Yak Yellow-Eyed-Penguin Yorkshire-Terrier"
zAn = "Zebra Zebra-Shark Zebu Zonkey Zorse"

adjDict['A'] = aStr.split(" ")
adjDict['B'] = bStr.split(" ")
adjDict['C'] = cStr.split(" ")
adjDict['D'] = dStr.split(" ")
adjDict['E'] = eStr.split(" ")
adjDict['F'] = fStr.split(" ")
adjDict['G'] = gStr.split(" ")
adjDict['H'] = hStr.split(" ")
adjDict['I'] = iStr.split(" ")
adjDict['J'] = jStr.split(" ")
adjDict['K'] = kStr.split(" ")
adjDict['L'] = lStr.split(" ")
adjDict['M'] = mStr.split(" ")
adjDict['N'] = nStr.split(" ")
adjDict['O'] = oStr.split(" ")
adjDict['P'] = pStr.split(" ")
adjDict['Q'] = qStr.split(" ")
adjDict['R'] = rStr.split(" ")
adjDict['S'] = sStr.split(" ")
adjDict['T'] = tStr.split(" ")
adjDict['U'] = uStr.split(" ")
adjDict['V'] = vStr.split(" ")
adjDict['W'] = wStr.split(" ")
adjDict['Y'] = yStr.split(" ")
adjDict['Z'] = zStr.split(" ")

animalDict['A'] = aAn.split(" ")
animalDict['B'] = bAn.split(" ")
animalDict['C'] = cAn.split(" ")
animalDict['D'] = dAn.split(" ")
animalDict['E'] = eAn.split(" ")
animalDict['F'] = fAn.split(" ")
animalDict['G'] = gAn.split(" ")
animalDict['H'] = hAn.split(" ")
animalDict['I'] = iAn.split(" ")
animalDict['J'] = jAn.split(" ")
animalDict['K'] = kAn.split(" ")
animalDict['L'] = lAn.split(" ")
animalDict['M'] = mAn.split(" ")
animalDict['N'] = nAn.split(" ")
animalDict['O'] = oAn.split(" ")
animalDict['P'] = pAn.split(" ")
animalDict['Q'] = qAn.split(" ")
animalDict['R'] = rAn.split(" ")
animalDict['S'] = sAn.split(" ")
animalDict['T'] = tAn.split(" ")
animalDict['U'] = uAn.split(" ")
animalDict['V'] = vAn.split(" ")
animalDict['W'] = wAn.split(" ")
animalDict['Y'] = yAn.split(" ")
animalDict['Z'] = zAn.split(" ")

userChoice = None
while not userChoice or userChoice != "Yes":
	userLoop()
	userChoice = str(raw_input("Type No to try again, or type Yes to end:\n"))






