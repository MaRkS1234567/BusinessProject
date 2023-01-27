'use strict';


class App extends React.Component {
  render() {
    function handleClick(img){
      var _=document.getElementById('img'); 
    }
    return (
      <div>
        <div className="p-17 p-md-5 mb-1 text-white rounded bg-dark centres">
            <img id="img" onClick={handleClick} className="img3" src="static/main/img/1.jpg" alt="1"/>
            <img onClick={handleClick} className="img top" src="static/main/img/3.jpg" alt="3"/>
            <img onClick={handleClick} className="img" src="static/main/img/7.jpeg" alt="7"/>
            <img onClick={handleClick} className="img" src="static/main/img/5.jpg" alt="5"/>
            <img onClick={handleClick} className="img" src="static/main/img/2.jpg" alt="2"/>
            <img onClick={handleClick} className="img delete2" src="static/main/img/6.jpeg" alt="6"/>
            <img onClick={handleClick} className="img bottom delete" src="static/main/img/8.jpeg" alt="8"/>
            <img onClick={handleClick} className="img4 delete" src="static/main/img/4.jpeg" alt="4"/>
            {/* <img className="img" src="static/main/img/8.jpeg" alt="8"/> */}
        </div><br/>
        <h3 className="text-center">Месторасположие</h3><br/> 
        <div className="p-17 p-md-5 mb-1 text-white rounded bg-dark d-flex">
          <p className="text-justify text2">
          База отдыха расположена в деревни Иваньково Владимирской области Александровского района, в 100 км от Москвы, в 20 км от районного центра города Александров. Также рядом с базой находится железно-дорожная станция Арсаки, что позволяет быстро и без машины добраться до базы .В рамках реализации проекта планируется выкупить дополнительную территорию под строительство домиков. Вблизи от базы расположены пруды. Рядом с базой расположен конный клуб Sokol Horse. Расположение вблизи городов ,входящих в  Золотое Кольцо России, позволяет посетить такие города, как Александров, Сергеев Посад и Переславль Залесский с его знаменитым Плещеевым озером. Также недалеко от базы располагается Засимова Пустынь - древний и очень красивый монастырь окруженный живописными пейзажами, что будет очень интересно как для паломников так и для простых туристов.   
          </p>
        </div><br/>
        <h3 className="text-center">Перечень услуг</h3><br/> 
        <div className="p-17 p-md-5 mb-1 text-white rounded 
        bg-dark d-flex">
          <p className="text-justify text2">
          На данный момент имеется гостевой дом, рассчитанный на проживание 1 семьи (2 взрослых и 2 детей) с 6 спальными местами (двумя односпальными кроватями на 2 этаже, одной двухспальной и раскладывающемся диваном), кухней, стиральной машиной, большой душевой кабиной и большими панорамными окнами. На участке также расположенно подсобное помещение с небольшой террасой где также можно воспользоваться мангалом в дождливое время, обустроенное место для отдыха на природе с мангалом и уличным обеденным столом. Также на территории расположена баня с возможностью окунуться в бассейн в летнее время, и игровой павильон с настольным теннисом, бильярдом, большим количеством настольных игр и конструктора для детей, а также камином, что позволяет пользоваться помещением в любое время года. Рядом с нами также расположена ферма со вкусными и натуральными продуктами. При отсутствии машины мы можем вывести гостей в самые интересные и красивые места. И также к нам можно заехать с собакой.   
          </p>
        </div><br/>
        <h3 className="text-center">Прайс-лист</h3><br/> 
        <div className="p-17 p-md-5 mb-1 text-white rounded bg-dark d-flex">
          <table className="t">
            <tr>
              <th>Наименование услуги</th>
              <th>Стоимость (руб)</th>
            </tr>
            <tr>
              <th>Аренда дома</th>
              <th>6000/сутки</th>
            </tr>
            <tr>
              <th>Игровой павильон</th>
              <th>1500/час</th>
            </tr>
            <tr>
              <th>Банная услуга</th>
              <th>2000/2 часа</th>
            </tr>
          </table>
            {/* <p className="p1">*Подробнее насчёт стоимости заказа уточняйте по номеру: 89104654371</p> */}
        </div>
      </div>
    );
  }
}

let domContainer = document.querySelector('#mainapp');
ReactDOM.render(<App />, domContainer);
