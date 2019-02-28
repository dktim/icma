$(function() {
	var serverTime = new Date(),
		stepWrapper = $('.steps .wrapper'),
		subStepWrapper = $('.sub-steps .wrapper');
	
	var stepsList = function(data) {
		stepWrapper.html('');
		for (var i in data) {
			var step = [
				'<div class="step">',
					'<div class="state"><i class="' + (data[i].state == '1' ? 'success-ico' : (data[i].state == '2' ? 'load-ico' : (data[i].state == '0' ? 'fail-ico' : 'wait-ico'))) + '"></i></div>',
					'<div class="text ' + (data[i].state == '1' ? 'success' : (data[i].state == '2' ? 'load' : (data[i].state == '0' ? 'fail' : ''))) + '">' + data[i].text + '</div>',
					'<div class="doshed ' + (data[i].state == '1' ? 'success' : (data[i].state == '2' ? 'load' : (data[i].state == '0' ? 'fail' : ''))) + '"></div>',
				'</div>'
			].join('');
			
			stepWrapper.append(step);
		}
		
		$('.doshed.load').each(function() {
			$(this).width($(this).parent().width() - $(this).siblings('.text').width() - $(this).siblings('.state').width() - 45).show();
		});
		
		var scrollEl = stepWrapper.find('.text.load');
		if (scrollEl.length > 0) {
			var scrollValue = scrollEl.offset().top + scrollEl.height() + stepWrapper.scrollTop() - stepWrapper.offset().top - stepWrapper.height();
			stepWrapper.animate({scrollTop: scrollValue}, 300);
		}
	},
	subStepList = function(data) {
		subStepWrapper.html('');
		
		for (var i in data) {
			var step = [
				'<div class="step">',
					'<div class="state"><i class="' + (data[i].state == '1' ? 'success-ico' : (data[i].state == '2' ? 'load-ico' : (data[i].state == '0' ? 'fail-ico' : 'wait-ico'))) + '"></i></div>',
					'<div class="text ' + (data[i].state == '1' ? 'success' : (data[i].state == '2' ? 'load' : (data[i].state == '0' ? 'fail' : ''))) + '">' + data[i].text + '</div>',
				'</div>'
			].join('');
			
			subStepWrapper.append(step);
		}
		
		var scrollEl = subStepWrapper.find('.text.load');
		if (scrollEl.length > 0) {
			var scrollValue = scrollEl.offset().top + scrollEl.height() + subStepWrapper.scrollTop() - subStepWrapper.offset().top - subStepWrapper.height();
			subStepWrapper.animate({scrollTop: scrollValue}, 300);
		}
	},
	getInfo = function() {
//		$.ajax({
//			url: '',
//			data: {t: new Date().getTime()},
//			dataType: 'json',
//			timeout: 10000,
//			type: 'POST',
//			success: function(data) {
				/* 测试数据-begin */
				var data = {serverTime: '235958', fzr: '李海军', zxr: '版本组'};
				/* 测试数据 -end*/
				formatTime(data.serverTime);
				$('#fzr').text(data.fzr);
				$('#zxr').text(data.zxr);
//			},
//			error: function() {
//				getInfo();
//			}
//		});
	},
	formatTime = function(time) {
		if (time.length != 6 || isNaN(time) || parseInt(time) > 240000 || parseInt(time) < 0) {
			timeDsq();
			return;
		}
		
		var hours = time.substring(0, 2),
			minutes = time.substring(2, 4),
			seconds = time.substring(4);
		
		serverTime.setHours(hours);
		serverTime.setMinutes(minutes);
		serverTime.setSeconds(seconds);
		
		timeDsq();
	},
	timeDsq = function() {
		$('.time').text((serverTime.getHours() > 9 ? serverTime.getHours() : '0' + serverTime.getHours()) + ':' + (serverTime.getMinutes() > 9 ? serverTime.getMinutes() : '0' + serverTime.getMinutes()));
		
		setTimeout(function() {
			serverTime.setSeconds(serverTime.getSeconds() + 1);
			timeDsq();
		}, 1000);
	},
	refresh = function() {
//		$.ajax({
//			url: '',
//			data: {t: new Date().getTime()},
//			dataType: 'json',
//			timeout: 10000,
//			type: 'POST',
//			success: function(data) {
				stepsList(data.stepData);
				subStepList(data.subStepData);
				/* 测试代码-begin */
				setTimeout(function() {
					for (var i in data.stepData) {
						if (data.stepData[i].state == '1' || data.stepData[i].state == '0') {
							continue;
						}
						if (data.stepData[i].state == '2') {
							var subFlag = true;
							for (var j in data.subStepData) {
								if (data.subStepData[j].state == '1' || data.subStepData[j].state == '0') {
									continue;
								}
								if (data.subStepData[j].state == '2') {
									data.subStepData[j].state = Math.floor(Math.random() * 2);
									if (data.subStepData[j].state == '0') {
										if ($('.step-fail').html() == '') {
											$('.step-fail').html('<span>1</span>项失败');
										} else {
											$('.step-fail span').text(parseInt($('.step-fail span').text()) + 1);
										}
									}
									continue;
								}
								if (data.subStepData[j].state == '3') {
									data.subStepData[j].state = '2';
									$('.step-num').text((parseInt(j) + 1) + '/' + data.subStepData.length);
									subFlag = false;
									break;
								}
							}
							if (subFlag) {
								data.stepData[i].state = Math.floor(Math.random() * 2);
							}
							break;
						}
						if (data.stepData[i].state == '3') {
							data.stepData[i].state = '2';
							for (var j in data.subStepData) {
								data.subStepData[j].state = '3';
							}
							$('.step-name').text(data.stepData[i].text);
							$('.step-num').text('1/' + data.subStepData.length);
							$('.step-fail').html('');
							var forecastTime = new Date(serverTime.getTime());
							forecastTime.setMinutes(forecastTime.getMinutes() + 30);
							$('.step-time').text('预计时间：' + (serverTime.getHours() > 9 ? serverTime.getHours() : '0' + serverTime.getHours()) + ':' + (serverTime.getMinutes() > 9 ? serverTime.getMinutes() : '0' + serverTime.getMinutes()) + '~' + (forecastTime.getHours() > 9 ? forecastTime.getHours() : '0' + forecastTime.getHours()) + ':' + (forecastTime.getMinutes() > 9 ? forecastTime.getMinutes() : '0' + forecastTime.getMinutes()));
							data.subStepData[0].state = '2';
							break;
						}
					}
					refresh();
				}, 3000);
				/* 测试代码 -end*/
//			},
//			complete: function() {
//				setTimeout(refresh, 3000);
//			}
//		});
	}
	
	getInfo();
	
	/* 测试数据-begin */
	var data = {
		stepData : [
			{text: '预投产准备', state: '3'},
			{text: '投产准备', state: '3'},
			{text: '投产', state: '3'},
			{text: '测试', state: '3'},
			{text: '扫码付验证', state: '3'},
			{text: '总结', state: '3'},
			{text: '总结2', state: '3'},
			{text: '总结3', state: '3'}
		],
		subStepData : [
			{text: '实名用户验证', state: '3'},
			{text: '非实名用户验证', state: '3'},
			{text: '余额查询', state: '3'},
			{text: '扣款', state: '3'},
			{text: '账户校对', state: '3'},
			{text: '测试1', state: '3'},
			{text: '测试2', state: '3'},
			{text: '测试3', state: '3'}
		]	
	};
	/* 测试数据 -end*/
	
	refresh();
});
