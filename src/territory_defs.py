TERRITORIES = {
    'Alaska': {
        'neighbors': ['Northwest Territory', 'Alberta', 'Kamchatka'],
        'continent': 'North America',
        'owner': None,
        'troops': 0
    },
    'Northwest Territory': {
        'neighbors': ['Alaska', 'Alberta', 'Ontario', 'Greenland'],
        'continent': 'North America',
        'owner': None,
        'troops': 0
    },
    'Greenland': {
        'neighbors': ['Northwest Territory', 'Ontario', 'Quebec', 'Iceland'],
        'continent': 'North America',
        'owner': None,
        'troops': 0
    },
    'Alberta': {
        'neighbors': ['Alaska', 'Northwest Territory', 'Ontario', 'Western United States'],
        'continent': 'North America',
        'owner': None,
        'troops': 0
    },
    'Ontario': {
        'neighbors': ['Northwest Territory', 'Alberta', 'Greenland', 'Quebec', 'Eastern United States', 'Western United States'],
        'continent': 'North America',
        'owner': None,
        'troops': 0
    },
    'Quebec': {
        'neighbors': ['Greenland', 'Ontario', 'Eastern United States'],
        'continent': 'North America',
        'owner': None,
        'troops': 0
    },
    'Western United States': {
        'neighbors': ['Alberta', 'Ontario', 'Eastern United States', 'Central America'],
        'continent': 'North America',
        'owner': None,
        'troops': 0
    },
    'Eastern United States': {
        'neighbors': ['Ontario', 'Quebec', 'Western United States', 'Central America'],
        'continent': 'North America',
        'owner': None,
        'troops': 0
    },
    'Central America': {
        'neighbors': ['Western United States', 'Eastern United States', 'Venezuela'],
        'continent': 'North America',
        'owner': None,
        'troops': 0
    },
    'Venezuela': {
        'neighbors': ['Central America', 'Peru', 'Brazil'],
        'continent': 'South America',
        'owner': None,
        'troops': 0
    },
    'Peru': {
        'neighbors': ['Venezuela', 'Brazil', 'Argentina'],
        'continent': 'South America',
        'owner': None,
        'troops': 0
    },
    'Brazil': {
        'neighbors': ['Venezuela', 'Peru', 'Argentina', 'North Africa'],
        'continent': 'South America',
        'owner': None,
        'troops': 0
    },
    'Argentina': {
        'neighbors': ['Peru', 'Brazil'],
        'continent': 'South America',
        'owner': None,
        'troops': 0
    },
    'Iceland': {
        'neighbors': ['Greenland', 'Scandinavia', 'Great Britain'],
        'continent': 'Europe',
        'owner': None,
        'troops': 0
    },
    'Scandinavia': {
        'neighbors': ['Iceland', 'Great Britain', 'Northern Europe', 'Ukraine'],
        'continent': 'Europe',
        'owner': None,
        'troops': 0
    },
    'Ukraine': {
        'neighbors': ['Scandinavia', 'Northern Europe', 'Southern Europe', 'Middle East', 'Afghanistan', 'Ural'],
        'continent': 'Europe',
        'owner': None,
        'troops': 0
    },
    'Great Britain': {
        'neighbors': ['Iceland', 'Scandinavia', 'Northern Europe', 'Western Europe'],
        'continent': 'Europe',
        'owner': None,
        'troops': 0
    },
    'Northern Europe': {
        'neighbors': ['Scandinavia', 'Ukraine', 'Southern Europe', 'Western Europe', 'Great Britain'],
        'continent': 'Europe',
        'owner': None,
        'troops': 0
    },
    'Western Europe': {
        'neighbors': ['Great Britain', 'Northern Europe', 'Southern Europe', 'North Africa'],
        'continent': 'Europe',
        'owner': None,
        'troops': 0
    },
    'Southern Europe': {
        'neighbors': ['Western Europe', 'Northern Europe', 'Ukraine', 'Middle East', 'Egypt', 'North Africa'],
        'continent': 'Europe',
        'owner': None,
        'troops': 0
    },
    'North Africa': {
        'neighbors': ['Brazil', 'Western Europe', 'Southern Europe', 'Egypt', 'East Africa', 'Congo'],
        'continent': 'Africa',
        'owner': None,
        'troops': 0
    },
    'Egypt': {
        'neighbors': ['North Africa', 'Southern Europe', 'Middle East', 'East Africa', 'Congo'],
        'continent': 'Africa',
        'owner': None,
        'troops': 0
    },
    'East Africa': {
        'neighbors': ['Egypt', 'North Africa', 'Congo', 'South Africa', 'Madagascar', 'Middle East'],
        'continent': 'Africa',
        'owner': None,
        'troops': 0
    },
    'Congo': {
        'neighbors': ['North Africa', 'East Africa', 'South Africa'],
        'continent': 'Africa',
        'owner': None,
        'troops': 0
    },
    'South Africa': {
        'neighbors': ['Congo', 'East Africa', 'Madagascar'],
        'continent': 'Africa',
        'owner': None,
        'troops': 0
    },
    'Madagascar': {
        'neighbors': ['South Africa', 'East Africa'],
        'continent': 'Africa',
        'owner': None,
        'troops': 0
    },
    'Ural': {
        'neighbors': ['Ukraine', 'Afghanistan', 'China', 'Siberia'],
        'continent': 'Asia',
        'owner': None,
        'troops': 0
    },
    'Siberia': {
        'neighbors': ['Ural', 'China', 'Mongolia', 'Irkutsk', 'Yakutsk'],
        'continent': 'Asia',
        'owner': None,
        'troops': 0
    },
    'Yakutsk': {
        'neighbors': ['Siberia', 'Irkutsk', 'Kamchatka'],
        'continent': 'Asia',
        'owner': None,
        'troops': 0
    },
    'Kamchatka': {
        'neighbors': ['Yakutsk', 'Irkutsk', 'Mongolia', 'Japan', 'Alaska'],
        'continent': 'Asia',
        'owner': None,
        'troops': 0
    },
    'Irkutsk': {
        'neighbors': ['Siberia', 'Yakutsk', 'Kamchatka', 'Mongolia'],
        'continent': 'Asia',
        'owner': None,
        'troops': 0
    },
    'Mongolia': {
        'neighbors': ['Siberia', 'Irkutsk', 'Kamchatka', 'Japan', 'China'],
        'continent': 'Asia',
        'owner': None,
        'troops': 0
    },
    'China': {
        'neighbors': ['Afghanistan', 'Ural', 'Siberia', 'Mongolia', 'Siam', 'India'],
        'continent': 'Asia',
        'owner': None,
        'troops': 0
    },
    'Afghanistan': {
        'neighbors': ['Ukraine', 'Ural', 'China', 'India', 'Middle East'],
        'continent': 'Asia',
        'owner': None,
        'troops': 0
    },
    'Middle East': {
        'neighbors': ['Ukraine', 'Afghanistan', 'India', 'Siam', 'Egypt', 'Southern Europe'],
        'continent': 'Asia',
        'owner': None,
        'troops': 0
    },
    'India': {
        'neighbors': ['Middle East', 'Afghanistan', 'China', 'Siam'],
        'continent': 'Asia',
        'owner': None,
        'troops': 0
    },
    'Siam': {
        'neighbors': ['India', 'China', 'Indonesia'],
        'continent': 'Asia',
        'owner': None,
        'troops': 0
    },
    'Japan': {
        'neighbors': ['Mongolia', 'Kamchatka'],
        'continent': 'Asia',
        'owner': None,
        'troops': 0
    },
    'Indonesia': {
        'neighbors': ['Siam', 'New Guinea', 'Western Australia'],
        'continent': 'Australia',
        'owner': None,
        'troops': 0
    },
    'New Guinea': {
        'neighbors': ['Indonesia', 'Western Australia', 'Eastern Australia'],
        'continent': 'Australia',
        'owner': None,
        'troops': 0
    },
    'Western Australia': {
        'neighbors': ['Indonesia', 'New Guinea', 'Eastern Australia'],
        'continent': 'Australia',
        'owner': None,
        'troops': 0
    },
    'Eastern Australia': {
        'neighbors': ['New Guinea', 'Western Australia'],
        'continent': 'Australia',
        'owner': None,
        'troops': 0
    },
    }

CONTIENENTS = {
    'North America': {
        'bonus': 5,
        'owner': None,
        "territories": ['Alaska', 'Northwest Territory', 'Greenland', 'Alberta', 'Ontario', 'Quebec', 'Western United States', 'Eastern United States', 'Central America']
    },
    'South America': {
        'bonus': 2,
        'owner': None,
        "territories": ['Venezuela', 'Peru', 'Brazil', 'Argentina']
    },
    'Europe': {
        'bonus': 5,
        'owner': None,
        "territories": ['Iceland', 'Scandinavia', 'Ukraine', 'Great Britain', 'Northern Europe', 'Western Europe', 'Southern Europe']
    },
    'Africa': {
        'bonus': 3,
        'owner': None,
        "territories": ['North Africa', 'Egypt', 'East Africa', 'Congo', 'South Africa', 'Madagascar']
    },
    'Asia': {
        'bonus': 7,
        'owner': None,
        "territories": ['Ural', 'Siberia', 'Yakutsk', 'Kamchatka', 'Irkutsk', 'Mongolia', 'China', 'Afghanistan', 'Middle East', 'India', 'Siam', 'Japan']
    },
    'Australia': {
        'bonus': 2,
        'owner': None,
        "territories": ['Indonesia', 'New Guinea', 'Western Australia', 'Eastern Australia']
    }
}

STARTING_TROOPS = 3