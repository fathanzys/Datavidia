def preprocessing_warmup(data):
    remove_column = [
        'Lahan Hutan',
        'Emisi Total',
        'Populasi Pedesaan',
        'Populasi Perkotaan',
        
    ]
    # Get total population = men total population + female total population
