from src.exceptions import DataFileError
def length_Filter (proteins,min_length,logg ):
    accepted=[]

    if not proteins :
        #logg.warning("any proteins is not in list  ")
        #this is for when list(proteins)was empty
        return accepted
    
    for n in proteins:
        #n is (Hamoon) proteins[i]
        
        if len(n.protein) >= min_length :
            accepted.append(n)
        else:
            logg.warning(f"protein '{n}' is not in range ")

    return accepted

def Read_to_dict_weight(amino_weights, logg):
    weight={}

    try:
        with open(amino_weights.txt, encoding="urf-8") as f:
            for line in enumerate(f,start=1):
                if line<6:
                    #the table of weight began in line=6 till end 
                    # & we have look to forward of line=6
                    continue
                else:
                    parts=line.split( )

                    if len(parts) !=2 :
                        #one error in logging
                        continue

                    amino=parts[0]
                    value=parts[1]
                        #managge of error about value {syntax}
                    weight[amino]=float[value]
                    
     
                return weight
    except:# talk to leader
           #Exception: return
    