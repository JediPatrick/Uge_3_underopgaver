def underopgaveTO():
    InfoFile = open('app_log (logfil analyse) 2_info.txt', 'w')
    WARNINGFile = open('app_log (logfil analyse) 2_Warning.txt', 'w')
    ERRORFile = open('app_log (logfil analyse) 2_Error.txt', 'w')
    SUCCESSFile = open('app_log (logfil analyse) 2_Success.txt', 'w')
    
    # Open the main log file for reading
    with open('app_log (logfil analyse) 2.txt', 'r') as file:
        for line in file:
            testLine = line[20:]  # Get the substring starting from index 20 to see if the lines is fx a success but its not picked up if an occurence is later in the line 
            if testLine.startswith('SUCCESS'):
                SUCCESSFile.write(f"{line}")
            elif testLine.startswith('WARNING'):
                WARNINGFile.write(f"{line}")
            elif testLine.startswith('ERROR'):
                ERRORFile.write(f"{line}")
            elif testLine.startswith('INFO'):
                InfoFile.write(f"{line}")
    
    # Closing the files is important
    InfoFile.close()
    WARNINGFile.close()
    ERRORFile.close()
    SUCCESSFile.close()