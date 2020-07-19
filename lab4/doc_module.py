def get_field(line, delim="\t", is_begin=True):
    """ Tokenize the line and returns the first token if
    parameter is_begin is true, returns the last token otherwise.

    :param line: The line string to tokenize
    :param delim: Delimiter to split tokens. Default is \t
    :param is_begin: Determine whether the first or the last token will be
        returned

    :return: Returns either the first or the last token depending on parameter
        is_begin
    """

    token = ""
    for c in line:
        if c != delim:
            token += c
        else:
            # Return first token if is_begin is true
            if is_begin:
                return token
            # If not, then continue to the next
            token = ""

    # Return the last token
    return token


def filter_hospital(
        hospital_name,
        doctor_data_filename,
        hospital_data_filename,
        outfilename
):
    """ Filter doctors by hospital name and write doctor id and daily
    number of patients of doctor in file

    :param hospital_name: Name of the hospital
    :param doctor_data_filename: Name of file containing doctor data
    :param hospital_data_filename: Name of file containing hospital data of
        a doctor
    :param outfilename: Name of file to write filtered data
    """

    # Open data files for reading and output file for writing
    with open(doctor_data_filename) as f_docdata, \
            open(hospital_data_filename) as f_hospitaldata, \
            open(outfilename, "a") as f_out:

        # We can skip first lines of both files, however, there is no need to
        # skip them since they won't satisfy the conditions below
        # f_docdata.readline()

        for doctor in f_docdata:
            # Strip the linebreak from line
            # If not stripped, get_field with is_begin=False, will result in
            # num_patients + the line break, and int() conversion will raise
            # an error
            doctor = doctor.strip("\n")

            doc_id = get_field(doctor)

            # To skip first line
            # f_hospitaldata.readline()

            for hospital in f_hospitaldata:
                # Strip the linebreak from line
                # Same reasoning with doctor
                hospital = hospital.strip("\n")

                if get_field(hospital) == doc_id:
                    doc_hospital = get_field(hospital, is_begin=False)
                    if doc_hospital == hospital_name:
                        f_out.write("{}\t{}\n".format(
                            doc_id,
                            int(get_field(doctor, is_begin=False)) // 30
                        ))
                    break

            # Put read cursor to the start of hospital data to read it again
            f_hospitaldata.seek(0)


def patient_averages(daily_patient_data_filename):
    """ Calculate average number of daily patients of doctors

    :param daily_patient_data_filename: Name of file containing doctor id and
        number of daily patients

    :return: Returns the calculated average
    """

    # Open file for reading
    with open(daily_patient_data_filename) as f_patientdata:
        total_patients = 0
        total_docs = 0
        for line in f_patientdata:
            # Strip the linebreak from line
            # Same reasoning with doctor and hospital
            line = line.strip("\n")

            total_patients += int(get_field(line, is_begin=False))
            total_docs += 1

    return total_patients / total_docs
