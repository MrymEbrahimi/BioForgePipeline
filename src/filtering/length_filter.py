from src.exceptions import DataFileError
def length_Filter (proteins,min_length,logg ):
    accepted=[]

    if not proteins :
<<<<<<< HEAD
        logg.warning("any proteins is not in list  ")
        return accepted
    
    for n in proteins:
        #n is (also) proteins[i]
=======
        #logg.warning("any proteins is not in list  ")
        #this is for when list(proteins)was empty
        return accepted
    
    for n in proteins:
        #n is (Hamoon) proteins[i]
>>>>>>> feature/filtering
        
        if len(n.protein) >= min_length :
            accepted.append(n)
        else:
            logg.warning(f"protein '{n}' is not in range ")
<<<<<<< HEAD
            continue
=======
>>>>>>> feature/filtering

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
                    line = line.strip()
                    parts=line.split( )

                    if len(parts) !=2 :
                        raise DataFileError(f"parts exist in this , {parts} isn't make from 2 parts")

                    amino=parts[0]
                    value=parts[1]
                        #managge of error about value {syntax}
                    weight[amino]=float[value]
                    
                return weight
    except Exception:
        return {}
        # talk to leader

def calleculate_weight(proteins,weight,min_weight,logg):
    result=[]

    for protein in proteins:
        sum_weight=0

        for amino in protein:
            sum_weight += weight[amino]

        sum_weight += 18.015

        if sum_weight < min_weight:
            continue

        result.append((protein , sum_weight))
            #check range of about sum_weight per protein was accepted

    return result
