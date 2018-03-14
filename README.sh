#On Debian 7.0

#Install build essentials
sudo apt-get install build-essential

#Install dependencies
sudo apt-get install binutils libproj-dev gdal-bin
sudo apt-get install libgeos-dev
sudo apt-get install libexpat1 libexpat1-dev
sudo apt-get install pkg-config
sudo apt-get install python2.7-dev # for pysqlite-2.6.3's C source

export "CFLAGS=-I/usr/local/include"
export "LDFLAGS=-L/usr/local/lib"


#Installing SQlite from source
wget http://sqlite.org/sqlite-amalgamation-3.6.23.1.tar.gz
tar xzf sqlite-amalgamation-3.6.23.1.tar.gz
cd sqlite-3.6.23.1
CFLAGS="-DSQLITE_ENABLE_RTREE=1" ./configure
make
sudo make install

#For raspberry
sudo apt-get install libgeos++

#Install libspatialite from source
wget http://www.gaia-gis.it/gaia-sins/libspatialite-sources/libspatialite-amalgamation-2.4.0-5.tar.gz
tar xzf libspatialite-amalgamation-2.4.0-5.tar.gz
cd libspatialite-amalgamation-2.4.0/
./configure --with-proj-include=/usr/include --with-proj-lib=/usr/lib --with-geos-include=/usr/include --with-geos-lib=/usr/lib
#or
./configure
make 
sudo make install 
#viola

#Install spatialite-tools-2.4.0
pkg-config --libs spatialite #check 

#for 'floor@@GLIBC_2.2.5' is defined in DSO error
export LDFLAGS="$LDFLAGS -lm"

wget http://www.gaia-gis.it/gaia-sins/spatialite-tools-sources/spatialite-tools-2.4.0-5.tar.gz
tar xzf spatialite-tools-2.4.0-5.tar.gz
cd spatialite-tools-2.4.0/
./configure
make
sudo make install

wget https://pypi.python.org/packages/source/p/pysqlite/pysqlite-2.6.3.tar.gz
tar xzf pysqlite-2.6.3.tar.gz
cd pysqlite-2.6.3
vim setup.cfg #comment
#must look like something like this:

#	[build_ext]
#	#define=
#	include_dirs=/usr/local/include
#	library_dirs=/usr/local/lib
#	libraries=sqlite3
#	#define=SQLITE_OMIT_LOAD_EXTENSION

sudo python setup.py install

# now run your Django project by
python manage.py runserver






