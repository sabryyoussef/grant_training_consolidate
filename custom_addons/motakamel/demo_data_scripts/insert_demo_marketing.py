#!/usr/bin/env python3
"""
Insert Motakamel Demo Marketing Data
"""

# Run in odoo shell: echo "exec(open('insert_demo_marketing.py').read())" | odoo-bin shell ...

try:
    print("\n" + "="*80)
    print("INSERTING MOTAKAMEL DEMO MARKETING DATA")
    print("="*80 + "\n")
    
    Program = env['motakamel.program']
    Marketing = env['motakamel.marketing']
    
    # Get the programs by code
    cbplc = Program.search([('program_code', '=', 'CBPLC')], limit=1)
    phri = Program.search([('program_code', '=', 'PHRI')], limit=1)
    pmp = Program.search([('program_code', '=', 'PMP')], limit=1)
    cbpcs = Program.search([('program_code', '=', 'CBPCS')], limit=1)
    cafm = Program.search([('program_code', '=', 'CAFM')], limit=1)
    
    if not all([cbplc, phri, pmp, cbpcs, cafm]):
        print("\n✗ Some programs are missing. Please create programs first.")
        exit(1)
    
    created_count = 0
    
    # CBPLC Marketing
    print(f"\nCreating marketing campaign for {cbplc.program_code}...")
    Marketing.create({
        'program_id': cbplc.id,
        'campaign_name': 'Q1 2025 Change Leadership Campaign',
        'featured_on_homepage': True,
        'featured_priority': 3,
        'show_on_catalog': True,
        'og_image_filename': 'cbplc_og_image.jpg',
        'seo_title': 'Certified Business Professional in Leading Through Change - IBTA Certification',
        'seo_description': "Master change management and organizational transformation with IBTA's Certified Business Professional in Leading Through Change. Hybrid training, bilingual support, 5-day program. Enroll now!",
        'seo_keywords': 'change management, leadership certification, IBTA, organizational change, transformation management, business professional, Cairo training',
        'canonical_url': 'https://www.yourcompany.com/programs/cbplc',
        'landing_page_url': '/programs/certified-business-professional-leading-through-change',
        'landing_page_template': 'modern',
        'call_to_action_text': 'احجز مقعدك الآن',
        'call_to_action_url': '/contactus?program=cbplc',
        'whatsapp_lead_link': 'https://wa.me/201234567890?text=أريد%20المزيد%20من%20المعلومات%20عن%20برنامج%20CBPLC',
        'lead_form_enabled': True,
        'lead_magnet_type': 'brochure',
        'brochure_pdf_filename': 'CBPLC_Brochure_2025.pdf',
        'promo_video_url': 'https://www.youtube.com/watch?v=cbplc2025',
        'testimonial_video_url': 'https://www.youtube.com/watch?v=cbplc_testimonials',
        'hashtags': '#ChangeManagement #Leadership #IBTA #Certification #CairoTraining',
        'facebook_post_text': '''🚀 Transform your leadership skills with IBTA's Certified Business Professional in Leading Through Change! 

✅ Master change management frameworks
✅ Build organizational resilience
✅ Lead successful transformations
✅ 5-day hybrid program in Cairo

Register now for our January 2026 session!
#CBPLC #ChangeManagement #Leadership''',
        'twitter_post_text': 'Master change management with IBTA CBPLC certification. 5-day hybrid program in Cairo. Transform organizations effectively. Register now! #ChangeManagement #Leadership',
        'linkedin_post_text': '''Are you ready to lead organizational transformation with confidence?

IBTA's Certified Business Professional in Leading Through Change (CBPLC) equips you with essential skills to navigate complex change initiatives.

📌 Program Highlights:
• Change management methodologies
• Stakeholder engagement strategies  
• Resilience-building techniques
• Practical case studies
• 5-day hybrid training in Cairo

Perfect for managers and leaders in both public and private sectors.

Learn more and register: [link]
#ChangeManagement #Leadership #IBTA #OrganizationalDevelopment''',
        'instagram_caption': '''Leading through change requires more than just strategy – it requires the right skills! 💼✨

Join our CBPLC certification program and become a transformation leader.

🎯 5-day hybrid training
📍 Cairo, Egypt
🌐 Bilingual (Arabic/English)

DM us for registration details!

#ChangeManagement #Leadership #IBTA #ProfessionalDevelopment #CairoTraining #BusinessTransformation''',
        'utm_source': 'website',
        'utm_medium': 'organic',
        'utm_campaign': 'cbplc_q1_2025',
        'google_analytics_id': 'G-CBPLC2025',
        'facebook_pixel_id': '123456789012345',
        'campaign_start_date': '2025-11-06',
        'campaign_end_date': '2026-01-09',
        'campaign_budget': 50000.0,
        'leads_generated': 125,
        'conversions': 18,
        'email_campaign_active': True,
        'drip_campaign_enabled': True,
        'campaign_status': 'active',
        'active': True,
    })
    created_count += 1
    print(f"  ✓ Created marketing campaign for {cbplc.program_code}")
    
    # PHRI Marketing
    print(f"\nCreating marketing campaign for {phri.program_code}...")
    Marketing.create({
        'program_id': phri.id,
        'campaign_name': 'PHRI International HR Certification 2025',
        'featured_on_homepage': True,
        'featured_priority': 2,
        'show_on_catalog': True,
        'og_image_filename': 'phri_og_image.jpg',
        'seo_title': 'Professional in Human Resources International (PHRI) - HRCI Certification Egypt',
        'seo_description': 'Earn your PHRI certification from HRCI. International HR credential recognized worldwide. Hybrid training in Cairo and Alexandria. 5-day intensive program with exam preparation.',
        'seo_keywords': 'PHRI, HRCI, human resources certification, international HR, HR professional, HR certification Egypt, Alexandria training',
        'canonical_url': 'https://www.yourcompany.com/programs/phri',
        'landing_page_url': '/programs/professional-human-resources-international',
        'landing_page_template': 'corporate',
        'call_to_action_text': 'سجل للحصول على شهادة PHRI',
        'call_to_action_url': '/contactus?program=phri',
        'whatsapp_lead_link': 'https://wa.me/201234567890?text=أريد%20المزيد%20من%20المعلومات%20عن%20شهادة%20PHRI',
        'lead_form_enabled': True,
        'lead_magnet_type': 'sample',
        'brochure_pdf_filename': 'PHRI_Program_Guide_2025.pdf',
        'promo_video_url': 'https://www.youtube.com/watch?v=phri2025',
        'testimonial_video_url': 'https://www.youtube.com/watch?v=phri_success',
        'hashtags': '#PHRI #HRCI #HumanResources #HRCertification #InternationalHR',
        'facebook_post_text': '🎓 Elevate your HR career with HRCI\'s PHRI certification! Global credential for HR professionals. 5-day hybrid program in Egypt. #PHRI #HRCI',
        'linkedin_post_text': 'Take Your HR Career Global with PHRI certification from HRCI. International HR expertise, comprehensive training, exam preparation included.',
        'instagram_caption': 'Your HR career deserves global recognition! PHRI certification from HRCI. 5-day hybrid program. Register now! #PHRI #HRCertification',
        'utm_source': 'website',
        'utm_medium': 'organic',
        'utm_campaign': 'phri_2025',
        'google_analytics_id': 'G-PHRI2025',
        'campaign_start_date': '2025-11-11',
        'campaign_end_date': '2026-01-24',
        'campaign_budget': 65000.0,
        'leads_generated': 87,
        'conversions': 14,
        'email_campaign_active': True,
        'campaign_status': 'active',
        'active': True,
    })
    created_count += 1
    print(f"  ✓ Created marketing campaign for {phri.program_code}")
    
    # PMP Marketing
    print(f"\nCreating marketing campaign for {pmp.program_code}...")
    Marketing.create({
        'program_id': pmp.id,
        'campaign_name': 'PMP Certification Premium Program 2025',
        'featured_on_homepage': True,
        'featured_priority': 1,
        'show_on_catalog': True,
        'og_image_filename': 'pmp_og_image.jpg',
        'seo_title': 'PMP Certification Training - Project Management Professional PMI Egypt',
        'seo_description': "Get your PMP certification from PMI. World's most recognized project management credential. 5-day hybrid training in Cairo. Includes 35 PDUs and exam preparation. Premium program.",
        'seo_keywords': 'PMP, PMI, project management certification, PMP Egypt, project manager, PMBOK, PMP training Cairo, 35 PDUs',
        'canonical_url': 'https://www.yourcompany.com/programs/pmp',
        'landing_page_url': '/programs/project-management-professional-pmp',
        'landing_page_template': 'modern',
        'call_to_action_text': 'ابدأ رحلتك للحصول على شهادة PMP',
        'call_to_action_url': '/contactus?program=pmp',
        'whatsapp_lead_link': 'https://wa.me/201234567890?text=أريد%20المزيد%20من%20المعلومات%20عن%20شهادة%20PMP',
        'lead_form_enabled': True,
        'lead_magnet_type': 'webinar',
        'brochure_pdf_filename': 'PMP_Premium_Package_2025.pdf',
        'promo_video_url': 'https://www.youtube.com/watch?v=pmp2025',
        'testimonial_video_url': 'https://www.youtube.com/watch?v=pmp_testimonials',
        'hashtags': '#PMP #PMI #ProjectManagement #PMPCertification #ProjectManager #Cairo',
        'facebook_post_text': '🚀 Become a Certified Project Management Professional! PMI\'s PMP - the gold standard. 35 PDUs + exam prep. Register now! #PMP #PMI',
        'twitter_post_text': 'Earn the world\'s #1 project management credential! PMP from PMI. 5-day premium training in Cairo. 35 PDUs + exam prep. #PMP #PMI',
        'linkedin_post_text': 'Ready to Join the Elite in Project Management? The PMP from PMI is the world\'s most recognized PM certification. Premium 5-day program in Cairo.',
        'instagram_caption': 'Level up your PM career! 📈 PMP certification = Career transformation. World\'s #1 PM credential. Premium training in Cairo. #PMP #PMI',
        'utm_source': 'website',
        'utm_medium': 'organic',
        'utm_campaign': 'pmp_premium_2025',
        'google_analytics_id': 'G-PMP2025',
        'facebook_pixel_id': '345678901234567',
        'campaign_start_date': '2025-11-16',
        'campaign_end_date': '2026-03-06',
        'campaign_budget': 95000.0,
        'leads_generated': 245,
        'conversions': 28,
        'email_campaign_active': True,
        'drip_campaign_enabled': True,
        'campaign_status': 'active',
        'active': True,
    })
    created_count += 1
    print(f"  ✓ Created marketing campaign for {pmp.program_code}")
    
    # CBPCS Marketing
    print(f"\nCreating marketing campaign for {cbpcs.program_code}...")
    Marketing.create({
        'program_id': cbpcs.id,
        'campaign_name': 'Customer Service Excellence Certification 2025',
        'featured_on_homepage': False,
        'show_on_catalog': True,
        'og_image_filename': 'cbpcs_og_image.jpg',
        'seo_title': 'Certified Business Professional in Customer Services - IBTA Certification',
        'seo_description': "Excel in customer service with IBTA's certification program. Learn advanced customer relationship management and service excellence. 5-day hybrid training in Cairo.",
        'seo_keywords': 'customer service certification, customer relations, service excellence, IBTA, customer experience, Cairo training',
        'canonical_url': 'https://www.yourcompany.com/programs/cbpcs',
        'landing_page_url': '/programs/certified-business-professional-customer-services',
        'landing_page_template': 'default',
        'call_to_action_text': 'احصل على شهادة خدمة العملاء',
        'call_to_action_url': '/contactus?program=cbpcs',
        'whatsapp_lead_link': 'https://wa.me/201234567890?text=أريد%20المزيد%20من%20المعلومات%20عن%20برنامج%20خدمة%20العملاء',
        'lead_form_enabled': True,
        'lead_magnet_type': 'brochure',
        'brochure_pdf_filename': 'CBPCS_Service_Excellence_2025.pdf',
        'promo_video_url': 'https://www.youtube.com/watch?v=cbpcs2025',
        'hashtags': '#CustomerService #ServiceExcellence #IBTA #CustomerExperience',
        'facebook_post_text': '⭐ Master customer service excellence! IBTA\'s CBPCS certification. 5-day training in Cairo. #CustomerService #IBTA',
        'linkedin_post_text': 'Excel in customer service with IBTA\'s certification. Master CRM, service quality, and customer experience optimization.',
        'instagram_caption': 'Transform customer experiences! ⭐ CBPCS certification. 5-day program in Cairo. #CustomerService #ServiceExcellence',
        'utm_source': 'website',
        'utm_medium': 'organic',
        'utm_campaign': 'cbpcs_2025',
        'google_analytics_id': 'G-CBPCS2025',
        'campaign_start_date': '2025-11-21',
        'campaign_end_date': '2026-02-20',
        'campaign_budget': 35000.0,
        'leads_generated': 95,
        'conversions': 22,
        'email_campaign_active': True,
        'campaign_status': 'active',
        'active': True,
    })
    created_count += 1
    print(f"  ✓ Created marketing campaign for {cbpcs.program_code}")
    
    # CAFM Marketing
    print(f"\nCreating marketing campaign for {cafm.program_code}...")
    Marketing.create({
        'program_id': cafm.id,
        'campaign_name': 'CAFM Facilities Management Certification 2025',
        'featured_on_homepage': False,
        'show_on_catalog': True,
        'og_image_filename': 'cafm_og_image.jpg',
        'seo_title': 'Certified Associate in Facilities Management - IFMA Certification Egypt',
        'seo_description': 'Start your facilities management career with IFMA\'s CAFM certification. Learn building operations, maintenance management, and workplace services. 5-day hybrid training in Cairo.',
        'seo_keywords': 'facilities management certification, CAFM, IFMA, building management, property management, workplace services, Cairo training',
        'canonical_url': 'https://www.yourcompany.com/programs/cafm',
        'landing_page_url': '/programs/certified-associate-facilities-management',
        'landing_page_template': 'default',
        'call_to_action_text': 'ابدأ مسيرتك في إدارة المرافق',
        'call_to_action_url': '/contactus?program=cafm',
        'whatsapp_lead_link': 'https://wa.me/201234567890?text=أريد%20المزيد%20من%20المعلومات%20عن%20شهادة%20CAFM',
        'lead_form_enabled': True,
        'lead_magnet_type': 'brochure',
        'brochure_pdf_filename': 'CAFM_Facilities_Guide_2025.pdf',
        'promo_video_url': 'https://www.youtube.com/watch?v=cafm2025',
        'testimonial_video_url': 'https://www.youtube.com/watch?v=cafm_careers',
        'hashtags': '#FacilitiesManagement #CAFM #IFMA #BuildingManagement #PropertyManagement',
        'facebook_post_text': '🏢 Launch your facilities management career! IFMA\'s CAFM certification. Professional training, international credential, 5-day program in Cairo. #CAFM #IFMA',
        'twitter_post_text': 'Start your FM career right! CAFM certification from IFMA. Building operations + maintenance + workplace services. 5-day training in Cairo. #CAFM #FacilitiesManagement',
        'linkedin_post_text': '''Build Your Career in Facilities Management with IFMA\'s CAFM Certification

Learn essential skills in:
• Building operations & maintenance
• Project coordination
• Sustainability practices
• Facility planning
• Workplace services

5-day hybrid program in Cairo with international recognition.

Register now and join the facilities management profession!
#FacilitiesManagement #CAFM #IFMA #PropertyManagement''',
        'instagram_caption': '''Ready to manage world-class facilities? 🏢

CAFM certification from IFMA equips you with the skills to excel in facilities management.

✅ Building operations
✅ Maintenance management
✅ Workplace services
✅ 5-day hybrid training

DM for details!
#CAFM #FacilitiesManagement #IFMA #CareerDevelopment #Cairo''',
        'utm_source': 'website',
        'utm_medium': 'organic',
        'utm_campaign': 'cafm_2025',
        'google_analytics_id': 'G-CAFM2025',
        'facebook_pixel_id': '567890123456789',
        'campaign_start_date': '2025-11-26',
        'campaign_end_date': '2026-03-01',
        'campaign_budget': 40000.0,
        'leads_generated': 68,
        'conversions': 16,
        'email_campaign_active': True,
        'drip_campaign_enabled': False,
        'campaign_status': 'active',
        'active': True,
    })
    created_count += 1
    print(f"  ✓ Created marketing campaign for {cafm.program_code}")
    
    env.cr.commit()
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    
    # Count marketing campaigns per program
    for prog in [cbplc, phri, pmp, cbpcs, cafm]:
        if prog:
            mkt_count = Marketing.search_count([('program_id', '=', prog.id)])
            mkts = Marketing.search([('program_id', '=', prog.id)])
            print(f"\n[{prog.program_code}] {prog.program_name}:")
            for mkt in mkts:
                print(f"  Campaign: {mkt.campaign_name}")
                print(f"    Budget: {int(mkt.campaign_budget):,} EGP")
                print(f"    Leads: {mkt.leads_generated} | Conversions: {mkt.conversions}")
                print(f"    Status: {mkt.campaign_status}")
                print(f"    Featured on Homepage: {'Yes' if mkt.featured_on_homepage else 'No'}")
    
    total_marketing = Marketing.search_count([])
    print(f"\n{'='*80}")
    print(f"Total marketing campaigns in database: {total_marketing}")
    print(f"Created in this session: {created_count}")
    
    print("\n" + "="*80)
    print("DEMO MARKETING DATA CREATED SUCCESSFULLY")
    print("="*80 + "\n")
    
except Exception as e:
    print(f"\n✗ ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
    env.cr.rollback()
