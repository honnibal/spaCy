cdef enum symbol_t:
    NIL
    IS_ALPHA
    IS_ASCII
    IS_DIGIT
    IS_LOWER
    IS_PUNCT
    IS_SPACE
    IS_TITLE
    IS_UPPER
    LIKE_URL
    LIKE_NUM
    LIKE_EMAIL
    IS_STOP
    IS_BRACKET
    IS_QUOTE
    IS_LEFT_PUNCT
    IS_RIGHT_PUNCT
    IS_CURRENCY

    FLAG19 = 19
    FLAG20
    FLAG21
    FLAG22
    FLAG23
    FLAG24
    FLAG25
    FLAG26
    FLAG27
    FLAG28
    FLAG29
    FLAG30
    FLAG31
    FLAG32
    FLAG33
    FLAG34
    FLAG35
    FLAG36
    FLAG37
    FLAG38
    FLAG39
    FLAG40
    FLAG41
    FLAG42
    FLAG43
    FLAG44
    FLAG45
    FLAG46
    FLAG47
    FLAG48
    FLAG49
    FLAG50
    FLAG51
    FLAG52
    FLAG53
    FLAG54
    FLAG55
    FLAG56
    FLAG57
    FLAG58
    FLAG59
    FLAG60
    FLAG61
    FLAG62
    FLAG63

    ID
    ORTH
    LOWER
    NORM
    SHAPE
    PREFIX
    SUFFIX

    LENGTH
    CLUSTER
    LEMMA
    POS
    TAG
    DEP
    ENT_IOB
    ENT_TYPE
    HEAD
    SENT_START
    SPACY
    PROB
    LANG

    ADJ
    ADP
    ADV
    AUX
    CONJ
    CCONJ # U20
    DET
    INTJ
    NOUN
    NUM
    PART
    PRON
    PROPN
    PUNCT
    SCONJ
    SYM
    VERB
    X
    EOL
    SPACE

    DEPRECATED001
    DEPRECATED002
    DEPRECATED003
    DEPRECATED004
    DEPRECATED005
    DEPRECATED006
    DEPRECATED007
    DEPRECATED008
    DEPRECATED009
    DEPRECATED010
    DEPRECATED011
    DEPRECATED012
    DEPRECATED013
    DEPRECATED014
    DEPRECATED015
    DEPRECATED016
    DEPRECATED017
    DEPRECATED018
    DEPRECATED019
    DEPRECATED020
    DEPRECATED021
    DEPRECATED022
    DEPRECATED023
    DEPRECATED024
    DEPRECATED025
    DEPRECATED026
    DEPRECATED027
    DEPRECATED028
    DEPRECATED029
    DEPRECATED030
    DEPRECATED031
    DEPRECATED032
    DEPRECATED033
    DEPRECATED034
    DEPRECATED035
    DEPRECATED036
    DEPRECATED037
    DEPRECATED038
    DEPRECATED039
    DEPRECATED040
    DEPRECATED041
    DEPRECATED042
    DEPRECATED043
    DEPRECATED044
    DEPRECATED045
    DEPRECATED046
    DEPRECATED047
    DEPRECATED048
    DEPRECATED049
    DEPRECATED050
    DEPRECATED051
    DEPRECATED052
    DEPRECATED053
    DEPRECATED054
    DEPRECATED055
    DEPRECATED056
    DEPRECATED057
    DEPRECATED058
    DEPRECATED059
    DEPRECATED060
    DEPRECATED061
    DEPRECATED062
    DEPRECATED063
    DEPRECATED064
    DEPRECATED065
    DEPRECATED066
    DEPRECATED067
    DEPRECATED068
    DEPRECATED069
    DEPRECATED070
    DEPRECATED071
    DEPRECATED072
    DEPRECATED073
    DEPRECATED074
    DEPRECATED075
    DEPRECATED076
    DEPRECATED077
    DEPRECATED078
    DEPRECATED079
    DEPRECATED080
    DEPRECATED081
    DEPRECATED082
    DEPRECATED083
    DEPRECATED084
    DEPRECATED085
    DEPRECATED086
    DEPRECATED087
    DEPRECATED088
    DEPRECATED089
    DEPRECATED090
    DEPRECATED091
    DEPRECATED092
    DEPRECATED093
    DEPRECATED094
    DEPRECATED095
    DEPRECATED096
    DEPRECATED097
    DEPRECATED098
    DEPRECATED099
    DEPRECATED100
    DEPRECATED101
    DEPRECATED102
    DEPRECATED103
    DEPRECATED104
    DEPRECATED105
    DEPRECATED106
    DEPRECATED107
    DEPRECATED108
    DEPRECATED109
    DEPRECATED110
    DEPRECATED111
    DEPRECATED112
    DEPRECATED113
    DEPRECATED114
    DEPRECATED115
    DEPRECATED116
    DEPRECATED117
    DEPRECATED118
    DEPRECATED119
    DEPRECATED120
    DEPRECATED121
    DEPRECATED122
    DEPRECATED123
    DEPRECATED124
    DEPRECATED125
    DEPRECATED126
    DEPRECATED127
    DEPRECATED128
    DEPRECATED129
    DEPRECATED130
    DEPRECATED131
    DEPRECATED132
    DEPRECATED133
    DEPRECATED134
    DEPRECATED135
    DEPRECATED136
    DEPRECATED137
    DEPRECATED138
    DEPRECATED139
    DEPRECATED140
    DEPRECATED141
    DEPRECATED142
    DEPRECATED143
    DEPRECATED144
    DEPRECATED145
    DEPRECATED146
    DEPRECATED147
    DEPRECATED148
    DEPRECATED149
    DEPRECATED150
    DEPRECATED151
    DEPRECATED152
    DEPRECATED153
    DEPRECATED154
    DEPRECATED155
    DEPRECATED156
    DEPRECATED157
    DEPRECATED158
    DEPRECATED159
    DEPRECATED160
    DEPRECATED161
    DEPRECATED162
    DEPRECATED163
    DEPRECATED164
    DEPRECATED165
    DEPRECATED166
    DEPRECATED167
    DEPRECATED168
    DEPRECATED169
    DEPRECATED170
    DEPRECATED171
    DEPRECATED172
    DEPRECATED173
    DEPRECATED174
    DEPRECATED175
    DEPRECATED176
    DEPRECATED177
    DEPRECATED178
    DEPRECATED179
    DEPRECATED180
    DEPRECATED181
    DEPRECATED182
    DEPRECATED183
    DEPRECATED184
    DEPRECATED185
    DEPRECATED186
    DEPRECATED187
    DEPRECATED188
    DEPRECATED189
    DEPRECATED190
    DEPRECATED191
    DEPRECATED192
    DEPRECATED193
    DEPRECATED194
    DEPRECATED195
    DEPRECATED196
    DEPRECATED197
    DEPRECATED198
    DEPRECATED199
    DEPRECATED200
    DEPRECATED201
    DEPRECATED202
    DEPRECATED203
    DEPRECATED204
    DEPRECATED205
    DEPRECATED206
    DEPRECATED207
    DEPRECATED208
    DEPRECATED209
    DEPRECATED210
    DEPRECATED211
    DEPRECATED212
    DEPRECATED213
    DEPRECATED214
    DEPRECATED215
    DEPRECATED216
    DEPRECATED217
    DEPRECATED218
    DEPRECATED219
    DEPRECATED220
    DEPRECATED221
    DEPRECATED222
    DEPRECATED223
    DEPRECATED224
    DEPRECATED225
    DEPRECATED226
    DEPRECATED227
    DEPRECATED228
    DEPRECATED229
    DEPRECATED230
    DEPRECATED231
    DEPRECATED232
    DEPRECATED233
    DEPRECATED234
    DEPRECATED235
    DEPRECATED236
    DEPRECATED237
    DEPRECATED238
    DEPRECATED239
    DEPRECATED240
    DEPRECATED241
    DEPRECATED242
    DEPRECATED243
    DEPRECATED244
    DEPRECATED245
    DEPRECATED246
    DEPRECATED247
    DEPRECATED248
    DEPRECATED249
    DEPRECATED250
    DEPRECATED251
    DEPRECATED252
    DEPRECATED253
    DEPRECATED254
    DEPRECATED255
    DEPRECATED256
    DEPRECATED257
    DEPRECATED258
    DEPRECATED259
    DEPRECATED260
    DEPRECATED261
    DEPRECATED262
    DEPRECATED263
    DEPRECATED264
    DEPRECATED265
    DEPRECATED266
    DEPRECATED267
    DEPRECATED268
    DEPRECATED269
    DEPRECATED270
    DEPRECATED271
    DEPRECATED272
    DEPRECATED273
    DEPRECATED274
    DEPRECATED275
    DEPRECATED276

    PERSON
    NORP
    FACILITY
    ORG
    GPE
    LOC
    PRODUCT
    EVENT
    WORK_OF_ART
    LANGUAGE
    LAW

    DATE
    TIME
    PERCENT
    MONEY
    QUANTITY
    ORDINAL
    CARDINAL

    acomp
    advcl
    advmod
    agent
    amod
    appos
    attr
    aux
    auxpass
    cc
    ccomp
    complm
    conj
    cop # U20
    csubj
    csubjpass
    dep
    det
    dobj
    expl
    hmod
    hyph
    infmod
    intj
    iobj
    mark
    meta
    neg
    nmod
    nn
    npadvmod
    nsubj
    nsubjpass
    num
    number
    oprd
    obj # U20
    obl # U20
    parataxis
    partmod
    pcomp
    pobj
    poss
    possessive
    preconj
    prep
    prt
    punct
    quantmod
    relcl
    rcmod
    root
    xcomp

    acl

    ENT_KB_ID
    MORPH
    ENT_ID

    IDX
    _
