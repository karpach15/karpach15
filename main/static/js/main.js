jQuery('document').ready(function(){
	var account_pic_url = $('.account_pic_url').text();
	$('.profile').css("background", "url(" + account_pic_url + ") no-repeat center top / cover");

	$('.driver:not(#driver_reg)').click(function(){
		$('.popUp').css('display', 'block');
		var driverName = $(this).find('#name').text();
		var driverSurname = $(this).find('#surname').text();
		var racesParticipated = $(this).find('#races_participated').text();
		var racesWon = $(this).find('#races_won').text();
		var regDate = $(this).find('#reg_date').text();
    	var about = $(this).find('#about').text();
    	var profilePic = $(this).find('#profilePic').css('background');
		
		var yearOfGDL = parseInt($(this).find('#year_of_getting_driving_licens').text());
		var monthOfGDL = (parseInt($(this).find('#month_of_getting_driving_licens').text())) - 1;
		var dayOfGDL = parseInt($(this).find('#day_of_getting_driving_licens').text());
		var dateOfGDL = (yearOfGDL + ', ' + monthOfGDL + ', ' + dayOfGDL);
		
		dateOfGDL = new Date(dateOfGDL);
		var today = new Date();
		
		var drivingExpMonths = Math.floor((today - dateOfGDL) / (30.5 * 24 * 60 * 60 * 1000));
		var drivingExpYears = Math.floor((today - dateOfGDL) / (365.25 * 24 * 60 * 60 * 1000));
		
		var years, months;

		if (drivingExpYears == 1){
			years = " год и ";
		}else{
			years = " лет и ";
		}

		if (drivingExpMonths == 1){
			months = " месяц";
		}else if (drivingExpMonths == 2 || drivingExpMonths == 3 || drivingExpMonths == 4){
			months = " месяца";
		}else{
			months = " месяцев";
		}

		if (drivingExpYears == 0){
			if (drivingExpMonths == 0){
				var drivingExp = "Меньше месяца";
			}else{
				var drivingExp = drivingExpMonths + months;
			}
		}else{
			var drivingExp = drivingExpYears + years + drivingExpMonths + months;
		}

    $('.driver_details #name').html(driverName);
    $('.driver_details #surname').html(driverSurname);
    $('.driver_details #races_participated span').html(racesParticipated);
    $('.driver_details #races_won span').html(racesWon);
    $('.driver_details #driving_exp span').html(drivingExp);
    $('.driver_details #reg_date span').html(regDate);
    $('.driver_details .about p').html(about);
    $('.driver_details .img').css('background', profilePic)
	});
	
	$('.close').click(function(){
		$('.popUp').css('display', 'none');
	});


	$('.drivers_list_btn').click(function(){
		$('.popUp').css('display', 'block');
	});
});
