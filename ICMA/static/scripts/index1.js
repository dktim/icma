$(function() {
	var curStepId = undefined,
		curStepName = undefined,
		refreshDsq = undefined,
		stepWrapper = $('.steps .wrapper'),
		subStepWrapper = $('.sub-steps .wrapper');
	
	var stepsList = function(data) {
		stepWrapper.html('');
		for (var i in data) {
			var step = [
				'<div class="step" data-id="' + data[i].id + '">',
					'<div class="state"><i class="' + (data[i].status == '2' ? 'success-ico' : (data[i].status == '1' ? 'load-ico' : (data[i].status == '3' ? 'fail-ico' : 'wait-ico'))) + '"></i></div>',
					'<div class="text ' + (data[i].status == '2' ? 'success' : (data[i].status == '1' ? 'load' : (data[i].status == '3' ? 'fail' : ''))) + '">' + data[i].name + '</div>',
					'<div class="doshed ' + (data[i].status == '2' ? 'success' : (data[i].status == '1' ? 'load' : (data[i].status == '3' ? 'fail' : ''))) + '"></div>',
				'</div>'
			].join('');
			
			stepWrapper.append(step);
			
			if (data[i].status == '1') {
				curStepId = data[i].id;
				curStepName = data[i].name;
			}
		}
		
		$('.doshed.load').each(function() {
			$(this).width($(this).parent().width() - $(this).siblings('.text').width() - $(this).siblings('.state').width() - 45).show();
		});
		
		var scrollEl = stepWrapper.find('.text.load');
		if (scrollEl.length > 0) {
			var scrollValue = scrollEl.offset().top + scrollEl.height() + stepWrapper.scrollTop() - stepWrapper.offset().top - stepWrapper.height();
			stepWrapper.animate({scrollTop: scrollValue}, 300);
		}
		
		$('.step').click(function() {
			curStepId = $(this).data('id');
			curStepName = $(this).find('.text').text();
			if (refreshDsq) {
				clearTimeout(refreshDsq);
				refreshDsq = undefined;
			}
			refresh();
		});
		
		refresh();
	},
	subStepList = function(data) {
		subStepWrapper.html('');
		
		var stepNum = 0,
			failNum = 0;
		
		for (var i in data) {
			var step = [
				'<div class="step">',
					'<div class="state"><i class="' + (data[i].status == '1' ? 'success-ico' : (data[i].status == '2' ? 'fail-ico' : 'wait-ico')) + '"></i></div>',
					'<div class="text ' + (data[i].status == '1' ? 'success' : (data[i].status == '2' ? 'fail' : '')) + '">' + data[i].name + '</div>',
				'</div>'
			].join('');
			
			subStepWrapper.append(step);
			
			if (data[i].status == '1') {
				stepNum++;
			} else if (data[i].status == '2') {
				stepNum++;
				failNum++;
			}
		}
		$('.step-num').text(stepNum + '/' + data.length);
		
		if (failNum > 0) {
			$('.step-fail').text(failNum + '项失败');	
		}
		else {
			   $('.step-fail').text('');

		}
		var scrollEl = subStepWrapper.find('.text.load');
		if (scrollEl.length > 0) {
			var scrollValue = scrollEl.offset().top + scrollEl.height() + subStepWrapper.scrollTop() - subStepWrapper.offset().top - subStepWrapper.height();
			subStepWrapper.animate({scrollTop: scrollValue}, 300);
		}
	},
	getInfo = function() {
		var p_id=$('.p_id').val()
		$.ajax({
			url: '/dashboard/task/'+p_id+'/',
			//data: {t: new Date().getTime(),'project_id':p_id},
			//data: {'project_id':p_id},
			dataType: 'json',
			timeout: 100000000,
			type: 'GET',
			success: function(data) {
				data = JSON.parse(data)
				for (var i in data ){
				}
				/* 测试数据-begin */
			/*	var data = [
						{id: '1', name: '预投产准备', status: '2'},
						{id: '2', name: '投产准备', status: '2'},
						{id: '3', name: '投产', status: '3'},
						{id: '4', name: '测试', status: '1'},
						{id: '5', name: '扫码付验证', status: '1'},
						{id: '6', name: '总结', status: '0'},
						{id: '7', name: '总结2', status: '0'},
						{id: '8', name: '总结3', status: '0'}
					];*/
				/* 测试数据 -end*/
				
				stepsList(data);
			},
			error: function() {
				getInfo();
			}
		});
	},
	timeDsq = function() {
		var serverTime = new Date();
		$('.time').text((serverTime.getHours() > 9 ? serverTime.getHours() : '0' + serverTime.getHours()) + ':' + (serverTime.getMinutes() > 9 ? serverTime.getMinutes() : '0' + serverTime.getMinutes()));
		
		setTimeout(function() {
			timeDsq();
		}, 100000);
	},
	refresh = function() {
	$.ajax({
			url: '/dashboard/subtask/'+curStepId+'/',
			//data: {id: curStepId, t: new Date().getTime()},
			dataType: 'json',
			timeout: 10000,
			type: 'GET',
		success: function(data) {
			//data=JSON.parse(data)
			
				/* 测试数据-begin */
			
				/* 测试数据 -end*/
				
				subStepList(data.substep);
				
				$('.step-name').text(curStepName);
				$('.step-time').text('预计时间：' + data.start_time + '~' + data.end_time);
				$('#fzr').text(data.charge_user);
				$('#zxr').text(data.execute_user);
			},
			complete: function() {
				refreshDsq = setTimeout(refresh, 300000);
		}
	});
	}
	timeDsq();
	getInfo();
	
	
});
