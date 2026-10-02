def length_Filter (proteins=['MKTA','TAF','KIUWDA'],min_length,logg ):
    accepted=[]

    if not proteins :
        #logg.warning("any proteins is not in list  ")
        #this is for when list(proteins)was empty
        return accepted
    
    for n in proteins:
        #n is (Hamoon) proteins[i]
        
        if len(n) >= min_length :
            accepted.append(n)
        else:
            logg.warning(f"protein '{n}' is not in range ")

    return accepted