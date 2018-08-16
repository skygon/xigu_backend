from django.http import HttpResponse, JsonResponse
from .models import Project, ProjectDescription
import os
import sys
# set import sys path
sys.path.append(os.path.join(os.path.dirname(__file__)))
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))

from xigu_utils import utils

def collect_project_info(p):
    data = {}
    data['project_id'] = p.id
    data['project_name'] = p.project_name
    data['project_type'] = p.project_type
    data['project_status'] = p.project_status
    data['tags'] = p.tags

    # 基金类数据
    if p.fund is not None:
        data['project_type'] = utils.FUND
        data['fund'] = {}
        
        data['fund']['seven_day_return'] = p.fund.seven_day_return
        data['fund']['estimate_yearly_return'] = p.fund.estimate_yearly_return
        data['fund']['history_yearly_return'] = p.fund.history_yearly_return
        
        data['fund']['min_amount'] = p.fund.min_amount
        data['fund']['step_amount'] = p.fund.step_amount
        data['fund']['invest_range'] = p.fund.invest_range
    elif p.insurance is not None:
        data['project_type'] = utils.INSURANCE
        data['insurance'] = {}
        data['insurance']['estimate_yearly_return'] = p.insurance.estimate_yearly_return
        
        data['insurance']['min_amount'] = p.insurance.min_amount
        data['insurance']['invest_range'] = p.insurance.invest_range
        data['insurance']['age_range'] = p.insurance.age_range
    elif p.real_estate is not None:
        data['project_type'] = utils.REAL_ESTATE
        data['real_estate'] = {}
        data['real_estate']['estimate_yearly_return'] = p.real_estate.estimate_yearly_return
        
        data['real_estate']['property_type'] = p.real_estate.property_type
        data['real_estate']['bedrooms'] = p.real_estate.bedrooms
        data['real_estate']['sqft'] = p.real_estate.sqft
    elif p.commercial_estate is not None:
        data['project_type'] = utils.COMMERCIAL_ESTATE
        data['commercial_estate'] = {}
        data['commercial_estate']['estimate_yearly_return'] = p.commercial_estate.estimate_yearly_return
        
        data['commercial_estate']['total_price'] = p.commercial_estate.total_price
        data['commercial_estate']['min_amount'] = p.commercial_estate.min_amount
        data['commercial_estate']['invest_range'] = p.commercial_estate.invest_range


    data['is_show'] = p.is_show
    return data

def get_yearly_return(project):
    try:
        data = {}
        if p.fund is not None:
            data['project_type'] = utils.FUND
            data['yearly_return'] = p.fund.estimate_yearly_return
        elif p.insurance is not None:
            data['project_type'] = utils.INSURANCE
            data['yearly_return'] = p.insurance.estimate_yearly_return
        elif p.real_estate is not None:
            data['project_type'] = utils.REAL_ESTATE
            data['yearly_return'] = p.real_estate.estimate_yearly_return
        elif p.commercial_estate is not None:
            data['project_type'] = utils.COMMERCIAL_ESTATE
            data['yearly_return'] = p.commercial_estate.estimate_yearly_return
        
        return data
    except Exception as e:
        utils.logger.debug('get yearly return fail %s', str(e))
        raise

def get_list(request):
    try:
        page_size = 10
        page_id = request.GET.get('page')
        if page_id is None or int(page_id) < 0:
            page_id = 1

        all_data = []
        total_count = Project.objects.count()

        start = (int(page_id) - 1) * page_size
        end = start + page_size
        #projects = Project.objects.all()[start:end]
        projects = Project.objects.order_by('-is_top')[start:end]

        for p in projects:
            data = collect_project_info(p)
            
            if data['is_show'] == 1:
                # already ordered by is_top value
                all_data.append(data)

        return utils.return_success(all_data, total_count)
    except Exception as e:
        utils.logger.debug('get project list fail: %s', str(e))
        return utils.return_error(400)

def get_detail(request):
    try:
        project_id = request.GET.get('id')
        p = Project.objects.get(id=project_id)
        response = HttpResponse()
   
        desc = p.project_detail.content
        new_content = desc.replace("src=\"/upload/upload/", "src=\"http://img.fang88.com/ng_server_upload/")
        
        response.write(new_content)
        return response

    except Exception as e:
        utils.logger.debug('get project detail fail: %s', str(e))
        return utils.return_error(400)