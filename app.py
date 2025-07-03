# --- Admin Dashboard Route ---
@app.route('/admin')
@login_required # Protect this route
def admin_dashboard():
    transactions = Transaction.query.order_by(Transaction.date_created.desc()).all()
    return render_template('admin_dashboard.html', transactions=transactions)
