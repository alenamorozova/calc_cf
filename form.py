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
        <form action="https://functions.yandexcloud.net/d4e9ii9enhs30rn8cfr6">
          <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label">Введите свой рост в сантиметрах</label>
            <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" name="height">
        
          </div>
          <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label">Введите свой вес</label>
            <input type="text" class="form-control" id="exampleInputPassword1" name="weight">
          </div>
  
          <button type="submit" class="btn btn-info center">Отправить</button>
        </form>
      </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
  </body>
</html>
"""


def handler(event, context):
    
    return {
        'statusCode': 200,
        'body': template,
    }
