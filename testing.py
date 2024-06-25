testing1 = ["LET Z 5",
            'GOTO "CZ"',
            "CCZ:    LET C 4",
            "PRINT C",
            "PRINT Z",
            "END",
            "CZ:     PRINT C",
            "PRINT Z",
            'GOTO "CCZ"',
            "."]

testing2 = ["LET Z 5", "."] # testing LET
testing3 = ["LET Z 5", "PRINT Z", "."]  # testing PRINT

testing4 = ["LET A 4", "ADD A 5", "."] # testing ADD
testing5 = ["LET A 5", "SUB A 3", "."] # testing SUB
testing6 = ["LET A 7", "MULT A 2", "."] # testing MUL
testing7 = ["LET A 8", "DIV A 2", "."] # testing DIV

# testing evaluate conditional (each conditional checking needs to evaluate to true)
testing8 = ["LET A 4", "GOTO 1 IF A < 5", "LET A 6", "."] # testing less than
testing9 = ["LET A 4", "GOTO 1 IF A <= 5", "LET A 6", "."] # testing less than or equal to
testing10 = ["LET A 8", "GOTO 1 IF A > 5", "LET A 6", "."] # testing greater than
testing11 = ["LET A 8", "GOTO 1 IF A >= 5", "LET A 6", "."] # testing greater than or equal to
testing12 = ["LET A 4", "GOTO 1 IF A = 4", "LET A 6", "."] # testing equal to
testing13 = ["LET A 0", "GOTO 1 IF A <> 4", "LET A 6", "."] # testing not equal to

testing14 = ["LET A 1",
             "GOSUB 5",
             "PRINT A",
             "END",
             "LET A 3",
             "RETURN",
             "PRINT A",
             "LET A 2",
             "GOSUB -4",
             "PRINT A",
             "RETURN",
             "."]

testing15 = ["LET A 5", "LET B 3", "ADD A B", "."]

testing16 = ["LET Z 1",
             "LET C 11",
             "LET F 4",
             'LET B "ZC"',
             "GOTO F IF F = 4",
             "ZC:     PRINT Z",
             "PRINT C",
             "END",
             "CZ:     PRINT C",
             "PRINT Z",
             "GOTO B",
             "."]

testing17 = ["INNUM X", "."]
testing18 = ["INNUM X", "."]
testing19 = ["INSTR X", "."]

testing20 = ["LET A 1", "GOTO A IF A = 1", "LET B 4", "."]