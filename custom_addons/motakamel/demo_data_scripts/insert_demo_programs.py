#!/usr/bin/env python3
"""
Insert Motakamel Demo Programs using SQL
"""

# Run in odoo shell: echo "exec(open('insert_demo_programs.py').read())" | odoo-bin shell ...

try:
    print("\n" + "="*80)
    print("INSERTING MOTAKAMEL DEMO PROGRAMS")
    print("="*80 + "\n")
    
    Program = env['motakamel.program']
    
    # Program 1: CBPLC
    print("Creating Program 1: CBPLC...")
    cbplc = Program.create({
        'program_id': 'PROG-00001',
        'program_name': 'Certified Business Professional in Leading Through Change',
        'program_name_ar': 'محترف أعمال معتمد في القيادة خلال التغيير',
        'program_code': 'CBPLC',
        'program_category': 'management',
        'program_level': 'advanced',
        'provider_name': 'IBTA',
        'provider_type': 'accredited',
        'description_en': '''<p>The Certified Business Professional in Leading Through Change program equips leaders and managers with essential skills to navigate organizational transformation effectively. This comprehensive certification covers change management methodologies, stakeholder engagement strategies, and resilience-building techniques.</p>
<p>Participants will learn to design and implement change initiatives, manage resistance, and create sustainable transformation outcomes. The program combines theoretical frameworks with practical case studies from leading organizations.</p>''',
        'description_ar': '''<p>يؤهل برنامج محترف أعمال معتمد في القيادة خلال التغيير القادة والمديرين بالمهارات الأساسية للتنقل في التحول التنظيمي بفعالية. تغطي هذه الشهادة الشاملة منهجيات إدارة التغيير واستراتيجيات مشاركة أصحاب المصلحة وتقنيات بناء المرونة.</p>
<p>سيتعلم المشاركون تصميم وتنفيذ مبادرات التغيير وإدارة المقاومة وإنشاء نتائج تحول مستدامة. يجمع البرنامج بين الأطر النظرية ودراسات الحالة العملية من المنظمات الرائدة.</p>''',
        'program_objective': 'Master change management frameworks, develop stakeholder engagement strategies, build organizational resilience, and lead successful transformation initiatives.',
        'career_outcome': 'Graduates can advance to senior leadership roles, change management positions, organizational development roles, and consulting positions in transformation management.',
        'status': 'published',
        'active': True,
        'visibility_scope': 'public',
        'display_order': 1,
        'internal_notes': 'Program launched in Q1 2025. High demand from public and private sectors. Featured program for leadership development.',
    })
    print(f"  ✓ Created: [{cbplc.program_code}] {cbplc.program_name}")
    
    # Program 2: PHRI
    print("Creating Program 2: PHRI...")
    phri = Program.create({
        'program_id': 'PROG-00002',
        'program_name': 'Professional in Human Resources – International',
        'program_name_ar': 'محترف في الموارد البشرية - دولي',
        'program_code': 'PHRI',
        'program_category': 'hr',
        'program_level': 'advanced',
        'provider_name': 'HRCI',
        'provider_type': 'accredited',
        'description_en': '''<p>The Professional in Human Resources – International (PHRI) certification is a globally recognized credential for HR professionals. This program validates expertise in HR operations, talent management, employee relations, and strategic HR planning.</p>
<p>PHRI certification demonstrates mastery of international HR practices and compliance standards. It is ideal for HR professionals seeking to advance their careers in multinational organizations or global HR consulting.</p>''',
        'description_ar': '''<p>شهادة محترف في الموارد البشرية - دولي (PHRI) هي اعتماد معترف به عالميًا لمتخصصي الموارد البشرية. يتحقق هذا البرنامج من الخبرة في عمليات الموارد البشرية وإدارة المواهب وعلاقات الموظفين والتخطيط الاستراتيجي للموارد البشرية.</p>
<p>تثبت شهادة PHRI إتقان ممارسات الموارد البشرية الدولية ومعايير الامتثال. إنها مثالية لمتخصصي الموارد البشرية الذين يسعون لتطوير مسيرتهم المهنية في المنظمات متعددة الجنسيات أو استشارات الموارد البشرية العالمية.</p>''',
        'program_objective': 'Achieve international HR certification, master global HR practices, understand compliance requirements, and develop strategic HR capabilities.',
        'career_outcome': 'Certified professionals can pursue roles as HR managers, HR business partners, talent acquisition specialists, and HR consultants in international organizations.',
        'status': 'published',
        'active': True,
        'visibility_scope': 'public',
        'display_order': 2,
        'internal_notes': 'Premium certification program. Requires renewal every 3 years. High market value in HR sector.',
    })
    print(f"  ✓ Created: [{phri.program_code}] {phri.program_name}")
    
    # Program 3: PMP
    print("Creating Program 3: PMP...")
    pmp = Program.create({
        'program_id': 'PROG-00003',
        'program_name': 'Project Management Professional',
        'program_name_ar': 'محترف إدارة المشاريع',
        'program_code': 'PMP',
        'program_category': 'management',
        'program_level': 'expert',
        'provider_name': 'PMI',
        'provider_type': 'accredited',
        'description_en': '''<p>The Project Management Professional (PMP) certification is the gold standard for project managers worldwide. This prestigious credential validates your ability to lead and direct projects, demonstrating mastery of project management knowledge and skills.</p>
<p>PMP certification covers the complete project lifecycle from initiation to closure, including scope, time, cost, quality, risk, and stakeholder management. It is recognized across industries and geographies as a mark of excellence in project management.</p>''',
        'description_ar': '''<p>شهادة محترف إدارة المشاريع (PMP) هي المعيار الذهبي لمديري المشاريع في جميع أنحاء العالم. يتحقق هذا الاعتماد المرموق من قدرتك على قيادة وتوجيه المشاريع، مما يثبت إتقان معرفة ومهارات إدارة المشاريع.</p>
<p>تغطي شهادة PMP دورة حياة المشروع الكاملة من البدء إلى الإغلاق، بما في ذلك إدارة النطاق والوقت والتكلفة والجودة والمخاطر وأصحاب المصلحة. يتم الاعتراف بها عبر الصناعات والجغرافيا كعلامة على التميز في إدارة المشاريع.</p>''',
        'program_objective': "Master PMI's project management framework, develop advanced project leadership skills, understand agile and predictive methodologies, and achieve globally recognized PMP certification.",
        'career_outcome': 'PMP-certified professionals can pursue senior project management roles, program management positions, portfolio management roles, and executive positions in project-driven organizations.',
        'status': 'published',
        'active': True,
        'visibility_scope': 'public',
        'display_order': 3,
        'internal_notes': 'Most popular certification. Premium pricing. Requires 35 PDUs for renewal every 3 years. High ROI for participants.',
    })
    print(f"  ✓ Created: [{pmp.program_code}] {pmp.program_name}")
    
    # Program 4: CBPCS
    print("Creating Program 4: CBPCS...")
    cbpcs = Program.create({
        'program_id': 'PROG-00004',
        'program_name': 'Certified Business Professional in Customer Services',
        'program_name_ar': 'محترف أعمال معتمد في خدمة العملاء',
        'program_code': 'CBPCS',
        'program_category': 'professional',
        'program_level': 'intermediate',
        'provider_name': 'IBTA',
        'provider_type': 'accredited',
        'description_en': '''<p>The Certified Business Professional in Customer Services program provides comprehensive training in customer relationship management, service excellence, and customer experience optimization. This certification is designed for professionals who interact directly with customers or manage customer service teams.</p>
<p>Participants learn service quality frameworks, complaint handling strategies, customer retention techniques, and digital customer service tools. The program emphasizes practical skills development through case studies and role-playing exercises.</p>''',
        'description_ar': '''<p>يوفر برنامج محترف أعمال معتمد في خدمة العملاء تدريبًا شاملاً في إدارة علاقات العملاء والتميز في الخدمة وتحسين تجربة العملاء. تم تصميم هذه الشهادة للمهنيين الذين يتفاعلون مباشرة مع العملاء أو يديرون فرق خدمة العملاء.</p>
<p>يتعلم المشاركون أطر جودة الخدمة واستراتيجيات التعامل مع الشكاوى وتقنيات الاحتفاظ بالعملاء وأدوات خدمة العملاء الرقمية. يركز البرنامج على تطوير المهارات العملية من خلال دراسات الحالة وتمارين لعب الأدوار.</p>''',
        'program_objective': 'Develop customer service excellence skills, master complaint resolution techniques, understand customer psychology, and achieve professional certification in customer services.',
        'career_outcome': 'Graduates can work as customer service managers, customer experience specialists, client relations officers, and service quality coordinators in various industries.',
        'status': 'published',
        'active': True,
        'visibility_scope': 'public',
        'display_order': 4,
        'internal_notes': 'Popular program for service sector. Good for both public and private sector employees. High enrollment in retail and hospitality.',
    })
    print(f"  ✓ Created: [{cbpcs.program_code}] {cbpcs.program_name}")
    
    # Program 5: CAFM
    print("Creating Program 5: CAFM...")
    cafm = Program.create({
        'program_id': 'PROG-00005',
        'program_name': 'Certified Associate in Facilities Management',
        'program_name_ar': 'زميل معتمد في إدارة المرافق',
        'program_code': 'CAFM',
        'program_category': 'technical',
        'program_level': 'intermediate',
        'provider_name': 'IFMA',
        'provider_type': 'accredited',
        'description_en': '''<p>The Certified Associate in Facilities Management (CAFM) program provides foundational knowledge in facilities and workplace management. This certification covers operations and maintenance, project management, sustainability, and facility planning.</p>
<p>CAFM is ideal for professionals beginning their careers in facilities management or those transitioning from related fields. The program emphasizes practical applications and industry best practices for managing physical assets and workplace environments.</p>''',
        'description_ar': '''<p>يوفر برنامج زميل معتمد في إدارة المرافق (CAFM) المعرفة الأساسية في إدارة المرافق وأماكن العمل. تغطي هذه الشهادة العمليات والصيانة وإدارة المشاريع والاستدامة وتخطيط المرافق.</p>
<p>CAFM مثالي للمهنيين الذين يبدأون حياتهم المهنية في إدارة المرافق أو أولئك الذين ينتقلون من مجالات ذات صلة. يركز البرنامج على التطبيقات العملية وأفضل الممارسات الصناعية لإدارة الأصول المادية وبيئات العمل.</p>''',
        'program_objective': 'Learn facilities management fundamentals, understand maintenance operations, develop project coordination skills, and achieve IFMA certification.',
        'career_outcome': 'Certified professionals can work as facilities coordinators, building managers, maintenance supervisors, and workplace services specialists.',
        'status': 'published',
        'active': True,
        'visibility_scope': 'public',
        'display_order': 5,
        'internal_notes': 'Entry-level facilities management certification. Good pathway to CFM certification. Growing demand in real estate sector.',
    })
    print(f"  ✓ Created: [{cafm.program_code}] {cafm.program_name}")
    
    env.cr.commit()
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    all_programs = Program.search([])
    print(f"Total programs in database: {len(all_programs)}")
    print("\nAll programs:")
    for p in all_programs:
        print(f"  - [{p.program_code}] {p.program_name} (Status: {p.status})")
    
    print("\n" + "="*80)
    print("DEMO PROGRAMS CREATED SUCCESSFULLY")
    print("="*80 + "\n")
    
except Exception as e:
    print(f"\n✗ ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
    env.cr.rollback()
