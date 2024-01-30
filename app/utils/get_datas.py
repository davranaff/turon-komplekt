from django.db.models import QuerySet, F


# dict[str, any] - any for <Model> types
def get_home_datas(model: dict[str, any], lc_type: str) -> dict[str, QuerySet]:

    info = model.get('info').objects.values(
        'email',
        'phone',
        'telegram',
        'instagram',
        'youtube',
        'pdf',
        title=F(f'title_{lc_type}'),
        subtitle=F(f'subtitle_{lc_type}'),
        about=F(f'about_{lc_type}'),
        address=F(f'address_{lc_type}'),
    ).first()

    projects = model.get('project').objects.values(
        'image',
        'slug',
        name=F(f'name_{lc_type}'),
        description=F(f'description_{lc_type}')
    ).all()[:8]

    certifications = model.get('certificate').objects.all()

    objects = model.get('object').objects.all()[:5]

    branches = model.get('branch').objects.all()

    trusts = model.get('trust').objects.all()

    return {
        'info': info,
        'projects': projects,
        'certifications': certifications,
        'objects': objects,
        'branches': branches,
        'trusts': trusts,
    }


def get_detail_data(model: dict, lc_type: str, slug: str) -> dict:

    project = model.get('project').objects.values(
        'image',
        'slug',
        name=F(f'name_{lc_type}'),
        description=F(f'description_{lc_type}')
    ).get(slug=slug)

    return {'project': project}


def get_all_products(model: dict, lc_type: str) -> dict:

    projects = model.get('project').objects.values(
        'image',
        'slug',
        name=F(f'name_{lc_type}'),
        description=F(f'description_{lc_type}')
    ).all()

    return {'projects': projects}
