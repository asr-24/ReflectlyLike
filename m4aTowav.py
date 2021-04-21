import os

from pydub import AudioSegment

initial = ['.m4a']


def changeOneFile():
    
    fromWhere = input("Input File name with the Location of the file - ")
    
    
    for i in range(len(fromWhere)-1,0,-1):
        if (fromWhere[i] == '\\'):
            sliceFromHere = i
            break      
        
    final = fromWhere.replace("m4a","wav")
    
    print(final)
    
    ourFile = fromWhere[sliceFromHere+1:]
    
    fromWhere = fromWhere[:sliceFromHere]


    
    
    for (dirpath, dirnames, filenames) in os.walk(fromWhere):
        if ourFile in filenames:
            i = filenames.index(ourFile)
            filename = filenames[i]
        
            if filename.endswith(tuple(initial)):
            
                filepath = dirpath + '/' + filename
                (path, file_extension) = os.path.splitext(filepath)
                file_extension_final = file_extension.replace('.', '')
                try:
                            track = AudioSegment.from_file(filepath,file_extension_final)
                            wav_filename = filename.replace(file_extension_final, 'wav')
                            wav_path = dirpath + '/' + wav_filename
                            print('CONVERTING: ' + str(filepath))
                            file_handle = track.export(wav_path, format='wav')
                            os.remove(filepath)
                            print("Done!")
                            return final
                        
                except:
                            print("ERROR CONVERTING " + str(filepath))
            
            else:    
                print("nu")
                
        
    
        




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    