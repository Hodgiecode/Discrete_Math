from task_01_01 import Task_01_01
from task_01_02 import Task_01_02
from task_01_03 import Task_01_03
from task_01_04 import Task_01_04
from task_01_05 import Task_01_05
from task_01_06 import Task_01_06
from task_01_07 import Task_01_07

from task_02_01 import Task_02_01
from task_02_02 import Task_02_02
from task_02_03 import Task_02_03
from task_02_05 import Task_02_05

from task_03_01 import Task_03_01
from task_03_02 import Task_03_02
from task_03_03 import Task_03_03

from task_04_01 import Task_04_01
from task_04_02 import Task_04_02
from task_04_03 import Task_04_03
from task_04_04 import Task_04_04
from task_04_05 import Task_04_05


def solve(value1,value2,data):
     if value1=="Миним.булевых функций":
        if value2=="Алгоритм Квайна-МакКласки":
            A=Task_04_01()
            t=A.main(data)
            return t
          
        if value2=="Алгоритм Блейка":
            A=Task_04_02()
            t=A.main(data)
            return t

        if value2=="Алгоритм Блейка 2":
            A=Task_04_03()
            t=A.main(data)
            return t

        if value2=="Ядро":
            A=Task_04_04()
            t=A.main(data)
            return t

        if value2=="Тупиковые ДНФ":
            A=Task_04_05()
            t=A.main(data)
            return t
			
     if value1=="Автоматы":
          if value2=="Состояния":
               A=Task_03_01()
               t=A.main(data)
               return t
          
          if value2=="Эквивалентность":
               A=Task_03_02()
               t=A.main(data)
               return t

          if value2=="Суперпозиция":
               A=Task_03_03()
               t=A.main(data)
               return t

     if value1=="K-значная логика":
         if value2=="Монотонность":
            A=Task_02_01()
            t=A.main(data)
            return str(t)
          
         if value2=="Сохранение":
            A=Task_02_02()
            t=A.main(data)
            return str(t)

         if value2=="Сохранение 2":
            A=Task_02_03()
            t=A.main(data)
            return str(t)

         if value2=="Шефферовость":
            A=Task_02_05()
            t=A.main(data)
            return str(t)

          
          
     if value1=="Алгебра логики":
        if value2=="Монотонность":
            A=Task_01_01()
            t=A.main(data)
            return str(t)

        if value2=="Линейность":
            A=Task_01_02()
            t=A.main(data)
            return str(t)

        if value2=="Самодвойственность":
            A=Task_01_03()
            t=A.main(data)
            return str(t)

        if value2=="Шефферовость":
            A=Task_01_04()
            t=A.main(data)
            return str(t)

        if value2=="Базис":
            A=Task_01_05()
            t=A.main(data)
            return str(t)
        
        if value2=="Полином Жегалкина":
            A=Task_01_06()
            t=A.main(data)
            return t

        if value2=="Оболочка":
            A=Task_01_07()
            t=A.main(data)
            return t
     
        

        
