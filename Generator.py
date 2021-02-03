import jinja2, os, sys
from datetime import datetime

def generate_defaults(template, contact_info, output_dir, build=False):
    version = 'Software'
    preset = 'OnePage'
    out = template.render(
        VERSION                    = version,
        PRESET                     = preset,
        ShowProjectFootNote        = True,
        MyEmail                    = contact_info['email'],
        MyPhone                    = contact_info['phone'],
        MyAddress                  = contact_info['address'],
        ShowPersonalContact        = True,
        ShowUrls                   = True,
        ShowTopBanner              = False,
        ShowTechnicalRange         = False,
        ShowEducationDetails       = True,
        ShowWorkExperienceDetails  = 1,
        ShowPublications           = True,
        ShowSkillsAndAbilities     = True,
        ShowHonorsAndAwards        = False,
        ShowHonorsAndAwardsDetails = 2,
        ShowProjects               = False,
        ShowProjectsDetails        = 1,
        CropDueToPageLimit         = False,
    )
    with open(f'{output_dir}/{version}_{preset}.tex', 'w') as f:
        f.write(out)
    if build:
        for i in range(2):
            os.system(f'pdflatex -output-directory={output_dir} -jobname=\'Resume_{version}_{preset}\' {output_dir}/{version}_{preset}.tex')

    version = 'Software'
    preset = 'TwoPages'
    out = template.render(
        VERSION                    = version,
        PRESET                     = preset,
        ShowProjectFootNote        = True,
        MyEmail                    = contact_info['email'],
        MyPhone                    = contact_info['phone'],
        MyAddress                  = contact_info['address'],
        ShowPersonalContact        = True,
        ShowUrls                   = True,
        ShowTopBanner              = False,
        ShowTechnicalRange         = False,
        ShowEducationDetails       = True,
        ShowWorkExperienceDetails  = 2,
        ShowPublications           = True,
        ShowSkillsAndAbilities     = True,
        ShowHonorsAndAwards        = True,
        ShowHonorsAndAwardsDetails = 2,
        ShowProjects               = True,
        ShowProjectsDetails        = 1,
        CropDueToPageLimit         = False,
    )
    with open(f'{output_dir}/{version}_{preset}.tex', 'w') as f:
        f.write(out)
    if build:
        for i in range(2):
            os.system(f'pdflatex -output-directory={output_dir} -jobname=\'Resume_{version}_{preset}\' {output_dir}/{version}_{preset}.tex')

    version = 'SoftAndHardware'
    preset = 'OnePage'
    out = template.render(
        VERSION                    = version,
        PRESET                     = preset,
        ShowProjectFootNote        = True,
        MyEmail                    = contact_info['email'],
        MyPhone                    = contact_info['phone'],
        MyAddress                  = contact_info['address'],
        ShowPersonalContact        = True,
        ShowUrls                   = True,
        ShowTopBanner              = False,
        ShowTechnicalRange         = False,
        ShowEducationDetails       = False,
        ShowWorkExperienceDetails  = 1,
        ShowPublications           = True,
        ShowSkillsAndAbilities     = True,
        ShowHonorsAndAwards        = False,
        ShowHonorsAndAwardsDetails = 2,
        ShowProjects               = False,
        ShowProjectsDetails        = 1,
        CropDueToPageLimit         = False,
    )
    with open(f'{output_dir}/{version}_{preset}.tex', 'w') as f:
        f.write(out)
    if build:
        for i in range(2):
            os.system(f'pdflatex -output-directory={output_dir} -jobname=\'Resume_{version}_{preset}\' {output_dir}/{version}_{preset}.tex')

    version = 'SoftAndHardware'
    preset = 'TwoPages'
    out = template.render(
        VERSION                    = version,
        PRESET                     = preset,
        ShowProjectFootNote        = True,
        MyEmail                    = contact_info['email'],
        MyPhone                    = contact_info['phone'],
        MyAddress                  = contact_info['address'],
        ShowPersonalContact        = True,
        ShowUrls                   = True,
        ShowTopBanner              = False,
        ShowTechnicalRange         = False,
        ShowEducationDetails       = True,
        ShowWorkExperienceDetails  = 2,
        ShowPublications           = True,
        ShowSkillsAndAbilities     = True,
        ShowHonorsAndAwards        = True,
        ShowHonorsAndAwardsDetails = 2,
        ShowProjects               = True,
        ShowProjectsDetails        = 1,
        CropDueToPageLimit         = True,
    )
    with open(f'{output_dir}/{version}_{preset}.tex', 'w') as f:
        f.write(out)
    if build:
        for i in range(2):
            os.system(f'pdflatex -output-directory={output_dir} -jobname=\'Resume_{version}_{preset}\' {output_dir}/{version}_{preset}.tex')

    version = 'SoftAndHardware'
    preset = 'NotForWork'
    out = template.render(
        VERSION                    = version,
        PRESET                     = preset,
        ShowProjectFootNote        = True,
        MyEmail                    = contact_info['email'],
        MyPhone                    = contact_info['phone'],
        MyAddress                  = contact_info['address'],
        ShowPersonalContact        = False,
        ShowUrls                   = True,
        ShowTopBanner              = False,
        ShowTechnicalRange         = False,
        ShowEducationDetails       = True,
        ShowWorkExperienceDetails  = 2,
        ShowPublications           = True,
        ShowSkillsAndAbilities     = True,
        ShowHonorsAndAwards        = True,
        ShowHonorsAndAwardsDetails = 2,
        ShowProjects               = True,
        ShowProjectsDetails        = 1,
        CropDueToPageLimit         = False,
    )
    with open(f'{output_dir}/{version}_{preset}.tex', 'w') as f:
        f.write(out)
    if build:
        for i in range(2):
            os.system(f'pdflatex -output-directory={output_dir} -jobname=\'Resume_{version}_{preset}\' {output_dir}/{version}_{preset}.tex')

##################################################################

if __name__ == '__main__':
    latex_jinja_env = jinja2.Environment(
    	block_start_string = '\BLOCK{',
    	block_end_string = '}',
    	variable_start_string = '\VAR{',
    	variable_end_string = '}',
    	comment_start_string = '\#{',
    	comment_end_string = '}',
    	line_statement_prefix = '%=',
    	line_comment_prefix = '%#',
    	trim_blocks = True,
    	autoescape = False,
        undefined = jinja2.StrictUndefined,
    	loader = jinja2.FileSystemLoader(os.path.abspath('.'))
    )

    template = latex_jinja_env.get_template('ResumeTemplate.tex')

    contact_info = {
        'email': '50459973+ly4096x@users.noreply.github.com',
        'phone': '+1-(000)-000-0000',
        'address': '100 Anonymous St, New York, NY 10001'
    }

    build = (len(sys.argv) >= 2)
    if len(sys.argv) >= 3:
        contact_info['email'] = sys.argv[2]

    output_dir = f"output/{contact_info['email']}-{datetime.now().strftime('%Y%m%d')}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if False: # custom format generation
        version = 'SoftAndHardware'
        preset = 'NotForWork'
        out = template.render(
            VERSION                    = version,
            PRESET                     = preset,
            ShowProjectFootNote        = True,
            MyEmail                    = contact_info['email'],
            MyPhone                    = contact_info['phone'],
            MyAddress                  = contact_info['address'],
            ShowPersonalContact        = False,
            ShowUrls                   = True,
            ShowTopBanner              = False,
            ShowTechnicalRange         = False,
            ShowEducationDetails       = True,
            ShowWorkExperienceDetails  = 2,
            ShowPublications           = True,
            ShowSkillsAndAbilities     = True,
            ShowHonorsAndAwards        = False,
            ShowHonorsAndAwardsDetails = 2,
            ShowProjects               = False,
            ShowProjectsDetails        = 2,
            CropDueToPageLimit         = False,
        )
        with open(f'{output_dir}/{version}_{preset}.tex', 'w') as f:
            f.write(out)
        if build:
            for i in range(2):
                os.system(f'pdflatex -output-directory={output_dir} -jobname=\'Resume_{version}_{preset}\' {output_dir}/{version}_{preset}.tex')
    else:
        generate_defaults(template, contact_info, output_dir, build=build)
