CREATE TABLE patients (patient_id INT, last_name varchar(30),
                                                 first_name varchar(30),
                                                            date_death date(YYYY-MM-DD),
                                                                       last_visit date(YYYY-MM-DD),
                                                                                  primary_key (patient_id));