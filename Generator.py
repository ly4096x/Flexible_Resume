import jinja2, os, sys, json
from datetime import datetime

def generate_defaults(template, contact_info, banner_msg, output_dir, build=False):
    version = 'Software'
    preset = 'OnePage'
    date = datetime.now().strftime('%Y%m%d')
    out = template.render(
        VERSION                    = version,
        PRESET                     = preset,
        DATE                       = date,
        ShowProjectFootNote        = True,
        MyEmail                    = contact_info['email'],
        MyPhone                    = contact_info['phone'],
        MyAddress                  = contact_info['address'],
        ShowPersonalContact        = True,
        ShowUrls                   = True,
        BannerMsg                  = banner_msg,
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
        DATE                       = date,
        ShowProjectFootNote        = True,
        MyEmail                    = contact_info['email'],
        MyPhone                    = contact_info['phone'],
        MyAddress                  = contact_info['address'],
        ShowPersonalContact        = True,
        ShowUrls                   = True,
        BannerMsg                  = banner_msg,
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
        DATE                       = date,
        ShowProjectFootNote        = True,
        MyEmail                    = contact_info['email'],
        MyPhone                    = contact_info['phone'],
        MyAddress                  = contact_info['address'],
        ShowPersonalContact        = True,
        ShowUrls                   = True,
        BannerMsg                  = banner_msg,
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
        DATE                       = date,
        ShowProjectFootNote        = True,
        MyEmail                    = contact_info['email'],
        MyPhone                    = contact_info['phone'],
        MyAddress                  = contact_info['address'],
        ShowPersonalContact        = True,
        ShowUrls                   = True,
        BannerMsg                  = '', # to prevent page overflow
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
        DATE                       = date,
        ShowProjectFootNote        = True,
        MyEmail                    = contact_info['email'],
        MyPhone                    = contact_info['phone'],
        MyAddress                  = contact_info['address'],
        ShowPersonalContact        = False,
        ShowUrls                   = True,
        BannerMsg                  = banner_msg,
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

    if len(sys.argv) >= 2:
        with open(sys.argv[1]) as f:
            contact_info = json.load(f)

    build = (len(sys.argv) >= 3)

    banner_msg = ''
    if len(sys.argv) >= 4:
        banner_msg = sys.argv[3]

    output_dir = f"output/{contact_info['email']}-{datetime.now().strftime('%Y%m%d')}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if False: # custom format generation
        version = 'SoftAndHardware'
        preset = 'NotForWork'
        date = datetime.now().strftime('%Y%m%d')
        out = template.render(
            VERSION                    = version,
            PRESET                     = preset,
            DATE                       = date,
            ShowProjectFootNote        = True,
            MyEmail                    = contact_info['email'],
            MyPhone                    = contact_info['phone'],
            MyAddress                  = contact_info['address'],
            ShowPersonalContact        = False,
            ShowUrls                   = True,
            BannerMsg                  = banner_msg,
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
        generate_defaults(template, contact_info, banner_msg, output_dir, build=build)

    # cleanup
    _, _, fns = next(os.walk(output_dir))
    for fn in fns:
        ext = fn.split('.')[-1]
        if ext != 'pdf':
            print(f'Removing "{output_dir}/{fn}"')
            os.remove(f'{output_dir}/{fn}')
