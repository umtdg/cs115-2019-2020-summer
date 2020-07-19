import doc_module

hospital_name = input("Enter hospital name: ")

hospital_docs_filename = f"{hospital_name}_docs.txt"
doc_module.filter_hospital(
    hospital_name,
    "doctor_data.txt",
    "hospital_data.txt",
    hospital_docs_filename
)

print("Average daily number of patients is {}".format(
    doc_module.patient_averages(hospital_docs_filename)
))
