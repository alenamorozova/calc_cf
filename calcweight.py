template = """
<!doctype html>
<html lang="ru">
  <head>
    <!-- Обязательные метатеги -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <title>mom_under_python</title>
  </head>
  <body>

    <div class="container">
      <header class="d-flex justify-content-center py-3">
        <ul class="nav nav-pills">
          <li class="nav-item"><a href="#" class="btn btn-info" aria-current="page">Главная</a></li>
        </ul>
      </header>
    </div>

    <div class="row">
      <div class="col-5">
      </div>
      <div class="col-2">
        {message}
      </div>
    </div>
    <div class="row">
      <div class="col-5">
      </div>
      <div class="col-2">
        <a href="https://functions.yandexcloud.net/d4euqd91savcmv1asr66" type="button" class="btn btn-info">Попробовать ещё раз</a>
      </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
  </body>
</html>
"""

def get_message(event):
    my_param = event['multiValueQueryStringParameters']
    height = my_param.get('height')
    weight = my_param.get('weight')
    if height and weight:
      try:
        height = float(height[0])
        weight = float(weight[0])
      except:
        return 'Вы ввели неверные данные'
    else:
      return 'Нет необходимых параметров, попробуйте ещё раз'

    bmi = round(weight / (height / 100)**2, 2)
    message = ''
    if bmi < 16:
        message = f'Ваш индекс массы тела {bmi}, у вас выраженный дефицит массы тела.'
    elif bmi < 18.5:
        message = f'Ваш индекс массы тела {bmi}, у вас недобор веса.'
    elif bmi < 25:
        message = f'Ваш индекс массы тела {bmi}, ваш вес в норме.'
    elif bmi < 30:
        message = f'Ваш индекс массы тела {bmi}, у вас избыточный вес.'
    elif bmi < 35:
        message = f'Ваш индекс массы тела {bmi}, у вас ожирение I степени.'
    elif bmi < 40:
        message = f'Ваш индекс массы тела {bmi}, у вас ожирение II степени.'
    else:
        message = f'Ваш индекс массы тела {bmi}, у вас ожирение III степени.'
    return message


def handler(event, context):  
    return {
        'statusCode': 200,
        'body': template.format(message=get_message(event)),
    }
