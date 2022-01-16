from buffer import Buffer
from characterreader import CharacterReader
from conditions.condition import Condition
from conditions.typescondition import TypesCondition
from initconditions import *
from tokens.tablesoftokens import TablesOfTokens
from tokens.workingwithtoken import WorkingWithToken


class Program:
    def __init__(self, code: str) -> None:
        self.__tables = TablesOfTokens()
        self.__buffer = Buffer()
        self.__reader = CharacterReader(code)
        self.__condition = Condition()
        self.__token = WorkingWithToken(self.__buffer, self.__tables)
        self.__init_conditions()

    def __init_conditions(self) -> None:
        self.__condition_h = ConditionH(self.__reader, self.__buffer, self.__token, self.__condition)
        self.__condition_i = ConditionI(self.__reader, self.__buffer, self.__token, self.__condition)
        self.__condition_n2 = ConditionN2(self.__reader, self.__buffer, self.__token, self.__condition)
        self.__condition_n8 = ConditionN8(self.__reader, self.__buffer, self.__token, self.__condition)
        self.__condition_n10 = ConditionN10(self.__reader, self.__buffer, self.__token, self.__condition)
        self.__condition_n16 = ConditionN16(self.__reader, self.__buffer, self.__token, self.__condition)
        self.__condition_b = ConditionB(self.__reader, self.__buffer, self.__token, self.__condition)
        self.__condition_o = ConditionO(self.__reader, self.__buffer, self.__token, self.__condition)
        self.__condition_d = ConditionD(self.__reader, self.__buffer, self.__token, self.__condition)
        self.__condition_hx = ConditionHX(self.__reader, self.__buffer, self.__token, self.__condition)
        self.__condition_e11 = ConditionE11(self.__reader, self.__buffer, self.__token, self.__condition)
        self.__condition_zn = ConditionZN(self.__reader, self.__buffer, self.__token, self.__condition)
        self.__condition_e12 = ConditionE12(self.__reader, self.__buffer, self.__token, self.__condition)
        self.__condition_e13 = ConditionE13(self.__reader, self.__buffer, self.__token, self.__condition)
        self.__condition_p1 = ConditionP1(self.__reader, self.__buffer, self.__token, self.__condition)
        self.__condition_p2 = ConditionP2(self.__reader, self.__buffer, self.__token, self.__condition)
        self.__condition_e21 = ConditionE21(self.__reader, self.__buffer, self.__token, self.__condition)
        self.__condition_e22 = ConditionE22(self.__reader, self.__buffer, self.__token, self.__condition)
        self.__condition_c1 = ConditionC1(self.__reader, self.__buffer, self.__token, self.__condition)
        self.__condition_c2 = ConditionC2(self.__reader, self.__buffer, self.__token, self.__condition)
        self.__condition_c3 = ConditionC3(self.__reader, self.__buffer, self.__token, self.__condition)
        self.__condition_m1 = ConditionM1(self.__reader, self.__buffer, self.__token, self.__condition)
        self.__condition_m2 = ConditionM2(self.__reader, self.__buffer, self.__token, self.__condition)
        self.__condition_og = ConditionOG(self.__reader, self.__buffer, self.__token, self.__condition)

    def run(self) -> None:
        while self.__condition.now != TypesCondition.V and self.__condition.now != TypesCondition.ER:
            self.__scanner()

    def __scanner(self) -> None:
        match self.__condition.now:
            case TypesCondition.H:
                self.__condition_h.action()

            case TypesCondition.I:
                self.__condition_i.action()

            case TypesCondition.N2:
                self.__condition_n2.action()

            case TypesCondition.N8:
                self.__condition_n8.action()

            case TypesCondition.N10:
                self.__condition_n10.action()

            case TypesCondition.N16:
                self.__condition_n16.action()

            case TypesCondition.B:
                self.__condition_b.action()

            case TypesCondition.O:
                self.__condition_o.action()

            case TypesCondition.D:
                self.__condition_d.action()

            case TypesCondition.HX:
                self.__condition_hx.action()

            case TypesCondition.E11:
                self.__condition_e11.action()

            case TypesCondition.ZN:
                self.__condition_zn.action()

            case TypesCondition.E12:
                self.__condition_e12.action()

            case TypesCondition.E13:
                self.__condition_e13.action()

            case TypesCondition.P1:
                self.__condition_p1.action()

            case TypesCondition.P2:
                self.__condition_p2.action()

            case TypesCondition.E21:
                self.__condition_e21.action()

            case TypesCondition.E22:
                self.__condition_e22.action()

            case TypesCondition.C1:
                self.__condition_c1.action()

            case TypesCondition.C2:
                self.__condition_c2.action()

            case TypesCondition.C3:
                self.__condition_c3.action()

            case TypesCondition.M1:
                self.__condition_m1.action()

            case TypesCondition.M2:
                self.__condition_m2.action()

            case TypesCondition.OG:
                self.__condition_og.action()
