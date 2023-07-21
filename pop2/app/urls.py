from django.urls import path
from app.views import home
from app import views 

urlpatterns = [

    path('', views.home, name = 'home'),
    path('private-limited-company-registration', views.Private_limited, name='private-limited-company-registration'),
    path('limited-liability-partnership-registration', views.limited_liability, name='limited-liability-partnership-registration'),
    path('one-person-company-registration-process-benefits', views.one_person, name='one-person-company-registration-process-benefits'),
    path('partnership-firm-registration-process-benefits', views.partnership, name='partnership-firm-registration-process-benefits'),
    path('sole-proprietorship-firm-registration-process-advantages-compliance', views.sole_proprietarship, name='sole-proprietorship-firm-registration-process-advantages-compliance'),
    path('establishing-indian-subsidiary-benefits-process-compliance', views.register_an, name='establishing-indian-subsidiary-benefits-process-compliance'),
    path('section-8-company-registration-guide', views.section_8, name='section-8-company-registration-guide'),
    path('producer-company-registration-features-benefits-compliance', views.producer_company, name='producer-company-registration-features-benefits-compliance'),
    path('nidhi-company-registration-requirements-compliance', views.nidhi_company, name='nidhi-company-registration-requirements-compliance'),
    path('trademark-registration-protection' , views.trademark_registration, name = 'trademark-registration-protection'),
    path('trademark-opposition', views.trademark_opposition, name='trademark-opposition'),
    path('trademark-objection-reply', views.trademark_objection, name = 'trademark-objection-reply'),
    path('trademark-renewal', views.trademark_renewal, name ='trademark-renewal'),
    path('trademark-asignment', views.trademark_ass, name ='trademark-asignment'),
    path('patent-search', views.patent_sear, name ='patent-search'),
    path('provisional-patent', views.provisional_patent, name ='provisional-patent'),
    path('permanent-patent', views.permanent_patent, name ='permanent-patent'),
    path('copyright-registration', views.copyright_reg, name ='copyright-registration'),
    path('design-registration', views.design_regi, name ='design-registration'),
    path('sole-proprietorship-to-partnership', views.proprietorship_to_par, name ='sole-proprietorship-to-partnership'),
    path('sole-proprietorship-to-llp', views.proprietorship_to_llp, name ='sole-proprietorship-to-llp'),
    path('sole-proprietorship-to-private-limited-company', views.proprietorship_to_pri, name ='sole-proprietorship-to-private-limited-company'),
    path('sole-proprietorship-to-opc', views.proprietorship_to_opc, name ='sole-proprietorship-to-opc'),
    path('partnership-to-llp', views.parternship_to_llp, name ='partnership-to-llp'),
    path('partnership-to-private-limited-company', views.parternship_to_private, name ='partnership-to-private-limited-company'),
    path('llp-to-private-limited-company', views.llp_to_private, name ='llp-to-private-limited-company'),
    path('opc-to-private-limited-company-conversion', views.opc_to_private, name ='opc-to-private-limited-company-conversion'),
    path('private-limited-company-to-llp-conversion', views.private_limited_company_to_llp, name ='private-limited-company-to-llp-conversion'),
    path('conversion-private-company-public-company', views.private_company_to_public, name ='conversion-private-company-public-company'),
    path('add-or-remove-a-director-company', views.add_or_reove_a_dir, name ='add-or-remove-a-director-company'),
    path('add-or-remove-a-partner-llp', views.add_or_reove_a_par, name ='add-or-remove-a-partner-llp'),
    path('change-business-activity', views.change_business, name ='change-business-activity'),
    path('change-registered-office', views.change_registered, name ='change-registered-office'),
    path('company-name-change', views.change_company_name, name ='company-name-change'),
    path('change-llp-agreement', views.change_llp_agr, name ='change-llp-agreement'),
    path('change-partnership-deed', views.change_partenership_de, name ='change-partnership-deed'),
    path('increase-authorised-share-capital', views.increase_authorised, name ='increase-authorised-share-capital'),
    path('close-a-private-limited-company', views.close_a_private_limited, name ='close-a-private-limited-company'),
    path('close-a-limited-liability-partnership', views.close_a_limited_liability, name ='close-a-limited-liability-partnership'),
    path('close-a-one-person-company', views.close_a_one_person, name ='close-a-one-person-company'),
    path('dissolve-a-parnership-farm', views.dissolve_a_par, name ='dissolve-a-parnership-farm'),
    path('gst-registration', views.gst_registration, name ='gst-registration'),
    path('import-export-license-india-guide', views.import_export_co, name ='import-export-license-india-guide'),
    path('startup-registration-process-benefits-eligibility-guide', views.startup_in, name ='startup-registration-process-benefits-eligibility-guide'),
    path('lut-under-gst', views.lut_under, name ='lut-under-gst'),
    path('ssi-msme-registration', views.ssi_msme, name ='ssi-msme-registration'),
    path('shop-establishment-registration', views.shop_est, name ='shop-establishment-registration'),
    path('professional-tax-registration', views.professional_tax, name ='professional-tax-registration'),
    path('pan-application', views.pan_application, name ='pan-application'),
    path('tan-application', views.tan_application, name ='tan-application'),
    path('fssai-basic-registration', views.fssai_application, name ='fssai-basic-registration'),
    path('esi-registration', views.esi_registration, name ='esi-registration'),
    path('pf-registration', views.pf_registraion, name ='pf-registration'),
    path('gem-registration', views.gem_registration, name ='gem-registration'),
    path('nsic-registration', views.nsic_re, name ='nsic-registration'),
    path('factory-license', views.factory_lic, name ='factory-license'),
    path('trade-license', views.trade_license, name ='trade-license'),
    path('drug-license', views.drug_li, name ='drug-license'),
    path('liquor-license', views.liquor, name ='liquor-license'),
    path('labour-license', views.labour, name ='labour-license'),
    path('ayush-license', views.ayush, name ='ayush-license'),
    path('iso-certification', views.iso_certi, name ='iso-certification'),
    path('arai-certification', views.arai_certi, name ='arai-certification'),
    path('i-cat-certification', views.i_cat, name ='i-cat-certification'),
    path('dir3-din-kyc-filling', views.dir3, name ='dir3-din-kyc-filling'),
    path('roc-return-filling-for-pvt-ltd', views.roc_return_fiiling_for_pvt, name ='roc-return-filling-for-pvt-ltd'),
    path('roc-return-filling-for-opc', views.roc_return_fiiling_for_opc, name ='roc-return-filling-for-opc'),
    path('roc-return-filling-for-llp', views.roc_return_fiiling_for_llp, name ='roc-return-filling-for-llp'),
    path('personal-or-individual-income-tax-filing', views.personal_or_individaul, name ='personal-or-individual-income-tax-filing'),
    path('business-income-tax-filing', views.business_income, name ='business-income-tax-filing'),
    path('company-income-tax-filing', views.company_income, name ='company-income-tax-filing'),
    path('tds-filing', views.tds_filing, name ='tds-filing'),
    path('gst-return-filing', views.gst_return, name ='gst-return-filing'),
    path('video', views.video, name ='video'),
    path('contact-us-ng-associates', views.contact, name ='contact-us-ng-associates'),
    path('incorporation-public-company-requirements-compliance', views.incorporation, name='incorporation-public-company-requirements-compliance'),
    path('trademarks-types-registration-uses', views.trademark_blog, name='trademarks-types-registration-uses'),
    path('goods-services-tax-gst-introduction-benefits-registration', views.gst_blog, name='goods-services-tax-gst-introduction-benefits-registration'),
    path('understanding-right-issues-features-benefits-process', views.right_issue, name='understanding-right-issues-features-benefits-process'),
    path('bonus-issue-guide-corporate-actions', views.bonus_issue, name='bonus-issue-guide-corporate-actions'),
    path('conversion-of-private-comapany-into-public-company', views.conversion_of_pri, name='conversion-of-private-comapany-into-public-company'),
    path('legal-process-of-change-your-company-name', views.legal_process_of_change, name='legal-process-of-change-your-company-name'),
    path('one-person-company-OPC-registraion-process', views.one_person_company_opc, name='one-person-company-OPC-registraion-process'),
    path('procedure-for-nidhi-company-registration-requirements-compliance', views.procedure_for_nidhi_company_registraion, name='procedure-for-nidhi-company-registration-requirements-compliance'),
    path('procedure-incorporation-public-company-requirements-compliance', views.procedure_incorporation_of, name='procedure-incorporation-public-company-requirements-compliance'),
    path('public-limited-to-private-limited-conversion', views.public_limited_into_private, name='public-limited-to-private-limited-conversion'),
    path('employee-stock-ownership-plans-benefits-implementation', views.employee_stock, name='employee-stock-ownership-plans-benefits-implementation'),
    path('secretarial-standard-1-companies-act-2013', views.secretarial, name='secretarial-standard-1-companies-act-2013'),
    path('promoters-pre-incorporation-contracts-definition-benefits', views.pre_incorporation, name='promoters-pre-incorporation-contracts-definition-benefits'),
    path('save-data', views.save_data, name='save-data')

]