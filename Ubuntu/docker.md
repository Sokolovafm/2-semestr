RabbitMQ

RabbitMQ - брокер сообщений с открытым исходным кодом Работу можно описать следующим образом: Издатель отправляет сообщение определенному обменнику Обменник маршрутизирует его в одну или несколько очередей в соответтвии с правилами между ним и очередью Очередь хранит хранит ссылку на сообщение. Само сообщение хранится в оперативной памяти или на диске. Когда потребидель готов получить сообщение из очереди на сервер создает копию соодщения по ссылке и отправляет Потребитель получает сообщение и отправляет брокеру подтверждение. Брокер, получив подтверждение, удаляет копию сообщения из очереди. Затем удаляет из оперативной памяти или с диска.
Docker-демон - сервер контейнеров, входящий в состав программных средств Docker. Демон управляет Docker-объектами.
Docker-клиент(Docker-client/CLI) - интерфейс взаимодействия пользователя с Docker-демоном.
Docker-образ - файл, включающий зависимости, сведения, конфигурацию для дальнейшего развертывания и инициализации контейнера.
Docker-файл - описание правил по сборке образа, в котором первая строка указывает на базовый образ.
Docker-контейнер - это легкий, автономный исполняемый пакет программного обеспечения, который включает в себя все необходимые для запуска приложения.

Пользователь отдает команду с полмощью клиентского интерфейса Docker-демону, развернутому на Docker-хосте. Например, скачать готовый образ из реестра с помощью команды docker pull. Взаимодействие между клиентом и демоном обеспечивает REST API. Демон может использовать публичный или частный реестры.

Происходит запуск образа Docker Engine проверяет существование образа. Если образ уже сущесьтвует локально, Docker использует его для нового контейнера. При его отсутствии выполняется скачивание с Docker Hub.
Создание контейнера из образа.
Разметка файловой системы и добавление слоя для записи.
Создание сетевого интерфейса.
Поиск и присвоение IP-адреса.
Запуск указанного процеса.
Захват ввода/вывода приложения.

InfluxDB
Бд временных рядов, исходя из названия, представляет собой системы баз данных, специально предназначенные для обработки информации, связанной со временем.
Для каждой точки, которую вы можете сохранить, у вас есть связанная с ней временная метка.

При добавлении новых записей в реляционную БД и при наличии в таблице индексов СУБД будет многократно переиндексировать данные для быстрого и эффективного доступа к ним. Как следствие, производительность со временем снижается. При этом увеличивается нагрузка, что приводит к трудностям при чтении данных.
База данных временных рядов оптимизирована для быстрого приёма данных. Такие системы используют индексацию данных, объединенных со временем. Как следствие, скорость загрузки не уменьшается со временем и остается достаточно стабильной.
