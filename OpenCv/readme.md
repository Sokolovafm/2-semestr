Для работы с файлами необходимо подключить заголовочный файл . В определены несколько классов и подключены заголовочные файлы — файловый ввод и — файловый вывод.

Файловый ввод/вывод аналогичен стандартному вводу/выводу, единственное отличие – это то, что ввод/вывод выполнятся не на экран, а в файл. Если ввод/вывод на стандартные устройства выполняется с помощью объектов cin и cout, то для организации файлового ввода/вывода достаточно создать собственные объекты, которые можно использовать аналогично операторам cin и cout.

Например, необходимо создать текстовый файл и записать в него строку Работа с файлами в С++. Для этого необходимо проделать следующие шаги:

создать объект класса ofstream; связать объект класса с файлом, в который будет производиться запись; записать строку в файл; закрыть файл. Почему необходимо создавать объект класса ofstream, а не класса ifstream? Потому, что нужно сделать запись в файл, а если бы нужно было считать данные из файла, то создавался бы объект класса ifstream.

Для работы с системной датой и временем используется библиотека ctime и chrono

    ofstream file;
    file.open("coordinat.txt", ios_base::app);
    unsigned long milliseconds_since_epoch = chrono::system_clock::now().time_since_epoch() / chrono::milliseconds(1);
    file << milliseconds_since_epoch << " " << x << " " << y << endl; file.close();

В этой части кода мы открываем наш txt файл и записываем в него системное время с помощью chrono, time_sincce_epoch и т.д. Так же, записываем в него координаты по х и у, к каждой точке своё время постановки на карту

    void my_mouse_callback(int event, int x, int y, int flags, void* param) 
    { 
      if (event == EVENT_LBUTTONDOWN) 
      {
        Mat* pImage = (Mat*)param;
        Mat image = *pImage;
        Point trackBox; trackBox = Point(x, y);
        ellipse(image, Point(x, y), Size(20, 17), -50, 100, 30, Scalar(0, 255, 255), 40, 8, 0);
      }
    }

С помощью этого кода мы обрабатываем нажатие правой кнопки мишы, после обработки на нашем изображении рисуется элипс с заданными параметрами.

    using System;
    using ClassLibrary1;
    namespace ConsoleAppTest 
    {
      class Program 
      { 
        static double MinAVG(double[] marks) 
        { 
          double sum = 0; 
          for (int i = 0; i < marks.Length; i++) 
          { 
            Console.WriteLine(marks[i]);
            sum += marks[i]; 
          } 
              double minavg = sum / marks.Length; 
              Console.WriteLine("minavg = " + minavg);
          return 0;
        }
     
     
        static void Main(string[] args)
        {
        double[] marks = {3, 3, 4, 5};
        MinAVG(marks);
        Library.test_function();
        Console.WriteLine("Hello World!");
        }
      }
    }
