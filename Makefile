dev:
	sed -i '1s/^\xEF\xBB\xBF//' /home/yukihara/workspace/odoo-fitdnu/odoo.conf && python3 odoo-bin -c odoo.conf
init:
	python3 odoo-bin -c odoo.conf -i base