create table user_kontakt
(
    id                  int auto_increment
        primary key,
    inputFamily         char(20)                            not null,
    inputName           char(20)                            not null,
    inputLastName       char(20)                            not null,
    inputPhone          int                                 null,
    inputDateBirthsday  date                                not null,
    inputShool          char(20)                            null,
    inputNumberShool    char(20)                            null,
    inputClass          char(20)                            null,
    inputCity           char(20)                            not null,
    inputRaion          char(20)                            null,
    inputTupeStreet     char(20)                            null,
    inputNameStreet     char(20)                            null,
    inputHome           char(10)                            null,
    inputCorpus         char(10)                            null,
    inputRoom           int                                 null,
    inputFatherFamyli   char(20)                            null,
    inputFatherName     char(20)                            null,
    inputFatherLastName char(20)                            null,
    inputFatherPhone    int                                 null,
    inputMatherFamyli   char(20)                            null,
    inputMatherName     char(20)                            null,
    inputMatherLastName char(20)                            null,
    inputMatherPhone    int                                 null,
    RegDate             timestamp default CURRENT_TIMESTAMP null
);