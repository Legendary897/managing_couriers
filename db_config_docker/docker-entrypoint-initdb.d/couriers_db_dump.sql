create table if not exists public.area (
	id serial primary key,
	area_info json not null
)


create table if not exists public.couriers (
	id SERIAL primary key,
	id_area int references area(id),
	couriers_info json not null
)

insert into public.area(area_info, name_zone)
values (
	'{
		"polygon": [
			[55.96754282162305, 92.88956026871624],
			[55.991219, 92.887420],
			[56.009215, 92.961263],
			[55.995194, 92.971252]
		]
	}',
	'Правый берег'
),
(
	'{
		"polygon": [
			[56.006896, 92.871714],
			[56.020505, 92.867738],
			[56.019068, 92.804557],
			[55.992828, 92.809500]
		]
	}',
	'Левый берег'
)